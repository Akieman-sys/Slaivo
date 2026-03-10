from datetime import datetime, timezone
from typing import Any


def _safe_get_first_message(payload: dict[str, Any]) -> dict[str, Any] | None:
    try:
        entries = payload.get("entry", [])
        if not entries:
            return None

        changes = entries[0].get("changes", [])
        if not changes:
            return None

        value = changes[0].get("value", {})
        messages = value.get("messages", [])
        if not messages:
            return None

        return messages[0]
    except (IndexError, AttributeError, TypeError):
        return None


def _safe_get_value_block(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        entries = payload.get("entry", [])
        changes = entries[0].get("changes", [])
        return changes[0].get("value", {})
    except (IndexError, AttributeError, TypeError):
        return {}


def normalize_whatsapp_message(payload: dict[str, Any]) -> dict[str, Any] | None:
    message = _safe_get_first_message(payload)
    if not message:
        return None

    value_block = _safe_get_value_block(payload)
    metadata = value_block.get("metadata", {})
    contacts = value_block.get("contacts", [])

    customer_name = None
    if contacts:
        customer_name = contacts[0].get("profile", {}).get("name")

    provider_message_id = message.get("id")
    from_phone = message.get("from")
    to_phone = metadata.get("display_phone_number")
    message_type = message.get("type", "unknown")

    text_body = None
    if message_type == "text":
        text_body = message.get("text", {}).get("body")

    timestamp_raw = message.get("timestamp")
    received_at = None
    if timestamp_raw:
        try:
            received_at = datetime.fromtimestamp(
                int(timestamp_raw), tz=timezone.utc
            ).isoformat()
        except (ValueError, TypeError):
            received_at = None

    dedupe_key = f"whatsapp:{provider_message_id}" if provider_message_id else None

    return {
        "provider_message_id": provider_message_id,
        "from_phone": from_phone,
        "to_phone": to_phone,
        "text_body": text_body,
        "message_type": message_type,
        "received_at": received_at,
        "source_channel": "whatsapp",
        "dedupe_key": dedupe_key,
        "customer_name": customer_name,
    }