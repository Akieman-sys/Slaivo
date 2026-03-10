from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse
import os
import json

from app.services.whatsapp_parser import normalize_whatsapp_message
from app.utils.tracking import extract_tracking_id
from app.repositories.shipments import find_shipment_by_tracking_id

router = APIRouter()


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

    print("=== WHATSAPP WEBHOOK RECEIVED ===")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    print("=== NORMALIZED MESSAGE ===")
    print(json.dumps(normalized_message, indent=2, ensure_ascii=False))

    tracking_id = None
    shipment = None

    if normalized_message:
        tracking_id = extract_tracking_id(normalized_message.get("text_body"))
        if tracking_id:
            shipment = find_shipment_by_tracking_id(tracking_id)

    print("=== TRACKING LOOKUP ===")
    print(json.dumps(
        {
            "tracking_id": tracking_id,
            "shipment_found": shipment is not None,
            "shipment": shipment,
        },
        indent=2,
        ensure_ascii=False,
        default=str,
    ))

    return {
        "status": "received",
        "normalized_message": normalized_message,
        "tracking_id": tracking_id,
        "shipment": shipment,
    }