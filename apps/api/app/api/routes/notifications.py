from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.repositories.shipments import find_shipment_by_tracking_id
from app.services.event_notifications import process_shipment_event_notification
from app.repositories.conversations import list_conversations

router = APIRouter()


class ShipmentEventRequest(BaseModel):
    tracking_id: str
    from_phone: str
    to_phone: str


@router.post("/shipment-event")
def trigger_shipment_event(body: ShipmentEventRequest):
    shipment = find_shipment_by_tracking_id(body.tracking_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")

    conversations = list_conversations()
    conversation = next(
        (c for c in conversations if c.get("related_shipment_id") == shipment["id"]),
        None,
    )

    result = process_shipment_event_notification(
        shipment=shipment,
        conversation_id=conversation["id"] if conversation else None,
        from_phone=body.from_phone,
        to_phone=body.to_phone,
    )

    return {
        "shipment": shipment,
        "result": result,
    }