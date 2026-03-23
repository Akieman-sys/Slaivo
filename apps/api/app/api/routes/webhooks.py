from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse
import os
import json

from app.core.logging import get_logger
from app.services.whatsapp_parser import normalize_whatsapp_message
from app.services.intent_router import detect_intent
from app.services.reply_builder import build_tracking_reply, build_knowledge_reply
from app.utils.tracking import extract_tracking_id
from app.repositories.shipments import find_shipment_by_tracking_id
from app.repositories.knowledge import find_active_knowledge_item
from app.repositories.conversations import (
    find_conversation_by_customer_phone,
    create_conversation,
    touch_conversation,
)
from app.repositories.messages import create_inbound_message

router = APIRouter()
logger = get_logger("slaivo.webhooks")


@router.get("/whatsapp", response_class=PlainTextResponse)
async def verify_whatsapp_webhook(
    hub_mode: str = Query(alias="hub.mode"),
    hub_verify_token: str = Query(alias="hub.verify_token"),
    hub_challenge: str = Query(alias="hub.challenge"),
):
    expected_token = os.getenv("WHATSAPP_VERIFY_TOKEN")

    if hub_mode != "subscribe":
        raise HTTPException(status_code=400, detail="Invalid hub.mode")

    if not expected_token:
        raise HTTPException(status_code=500, detail="WHATSAPP_VERIFY_TOKEN not set")

    if hub_verify_token != expected_token:
        raise HTTPException(status_code=403, detail="Invalid verify token")

    return hub_challenge


@router.post("/whatsapp")
async def receive_whatsapp_webhook(request: Request):
    payload = await request.json()
    normalized_message = normalize_whatsapp_message(payload)

    logger.info("WhatsApp webhook received")
    logger.info(json.dumps(payload, indent=2, ensure_ascii=False))

    logger.info("Normalized message")
    logger.info(json.dumps(normalized_message, indent=2, ensure_ascii=False, default=str))

    intent = "unknown"
    reply = None
    shipment = None
    tracking_id = None
    conversation = None
    inbound_message = None

    if normalized_message:
        text_body = normalized_message.get("text_body")
        intent = detect_intent(text_body)

        if intent == "tracking_lookup":
            tracking_id = extract_tracking_id(text_body)
            if tracking_id:
                shipment = find_shipment_by_tracking_id(tracking_id)
            reply = build_tracking_reply(shipment)

        elif intent == "pricing_query":
            item = find_active_knowledge_item("pricing")
            reply = build_knowledge_reply(
                item,
                "Tarif indisponible pour le moment. Un agent pourra vous assister.",
            )

        elif intent == "warehouse_address":
            item = find_active_knowledge_item("warehouse_address")
            reply = build_knowledge_reply(
                item,
                "Adresse indisponible pour le moment. Un agent pourra vous assister.",
            )

        elif intent == "departure_query":
            item = find_active_knowledge_item("departure_info")
            reply = build_knowledge_reply(
                item,
                "Information de départ indisponible pour le moment. Un agent pourra vous assister.",
            )

        else:
            reply = {
                "reply_type": "unknown_intent",
                "message": "Je n’ai pas compris votre demande. Un agent pourra vous assister.",
                "should_escalate": True,
            }

        from_phone = normalized_message.get("from_phone")
        to_phone = normalized_message.get("to_phone")
        related_shipment_id = shipment["id"] if shipment else None

        conversation = find_conversation_by_customer_phone(from_phone)
        if not conversation:
            conversation = create_conversation(
                customer_phone=from_phone,
                related_shipment_id=related_shipment_id,
                priority="medium" if reply and reply.get("should_escalate") else "low",
            )
        else:
            touch_conversation(conversation["id"])

        inbound_message = create_inbound_message(
            conversation_id=conversation["id"],
            provider_message_id=normalized_message.get("provider_message_id"),
            message_type=normalized_message.get("message_type") or "text",
            text_body=normalized_message.get("text_body"),
            intent=intent,
            from_phone=from_phone,
            to_phone=to_phone,
            raw_payload=payload,
            related_shipment_id=related_shipment_id,
            dedupe_key=normalized_message.get("dedupe_key"),
            received_at=normalized_message.get("received_at"),
        )

    logger.info(f"Intent detected: {intent}")
    logger.info(json.dumps(reply, indent=2, ensure_ascii=False, default=str))

    return {
        "status": "received",
        "normalized_message": normalized_message,
        "intent": intent,
        "tracking_id": tracking_id,
        "shipment": shipment,
        "conversation": conversation,
        "inbound_message": inbound_message,
        "reply": reply,
    }