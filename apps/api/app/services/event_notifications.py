from app.repositories.event_notifications import (
    create_event_notification,
    find_recent_event_notification,
)
from app.repositories.messages import create_system_outbound_message


def build_event_message(shipment: dict) -> tuple[str | None, str | None]:
    status = shipment.get("status")
    tracking_id = shipment.get("tracking_id")
    balance = shipment.get("balance")
    currency = shipment.get("currency")

    if status == "ARRIVED_KIN":
        message = f"Bonjour, votre colis {tracking_id} est arrivé. Prochaine étape : récupération."
        if balance is not None and currency:
            message += f" Solde restant : {balance} {currency}."
        return "ARRIVED_KIN", message

    if status == "READY_FOR_PICKUP":
        message = f"Bonjour, votre colis {tracking_id} est prêt à être récupéré."
        if balance is not None and currency:
            message += f" Solde restant : {balance} {currency}."
        return "READY_FOR_PICKUP", message

    return None, None


def process_shipment_event_notification(
    shipment: dict,
    conversation_id: str | None,
    from_phone: str,
    to_phone: str,
) -> dict:
    event_type, message_text = build_event_message(shipment)

    if not event_type or not message_text:
        return {
            "status": "ignored",
            "reason": "unsupported_status",
        }

    shipment_id = shipment["id"]
    cooldown_key = f"{shipment_id}:{event_type}"

    recent = find_recent_event_notification(shipment_id, event_type)
    if recent:
        blocked = create_event_notification(
            shipment_id=shipment_id,
            conversation_id=conversation_id,
            event_type=event_type,
            status="blocked",
            cooldown_key=cooldown_key,
            message_text=message_text,
            failure_reason="cooldown_active",
        )
        return {
            "status": "blocked",
            "event_notification": blocked,
        }

    notification = create_event_notification(
        shipment_id=shipment_id,
        conversation_id=conversation_id,
        event_type=event_type,
        status="pending",
        cooldown_key=cooldown_key,
        message_text=message_text,
    )

    outbound_message = None
    if conversation_id:
        outbound_message = create_system_outbound_message(
            conversation_id=conversation_id,
            from_phone=from_phone,
            to_phone=to_phone,
            text_body=message_text,
            trigger_type="relance_event",
            related_shipment_id=shipment_id,
        )

    return {
        "status": "created",
        "event_notification": notification,
        "message": outbound_message,
    }