def build_tracking_reply(shipment: dict | None) -> dict:
    if not shipment:
        return {
            "reply_type": "tracking_not_found",
            "message": "Tracking introuvable.",
            "should_escalate": True,
        }

    status = shipment.get("status")
    eta = shipment.get("eta")
    balance = shipment.get("balance")
    currency = shipment.get("currency")

    next_action = {
        "ARRIVED_KIN": "Récupération",
        "READY_FOR_PICKUP": "Passez récupérer votre colis",
        "IN_TRANSIT": "Attendre l’arrivée",
        "DELIVERED": "Colis livré",
    }.get(status, "Attendre la prochaine mise à jour")

    message = f"Votre colis {shipment.get('tracking_id')} est actuellement {status}."

    if eta:
        message += f" ETA : {eta}."

    message += f" Prochaine étape : {next_action}."

    if balance is not None and currency:
        message += f" Solde restant : {balance} {currency}."

    return {
        "reply_type": "tracking_reply",
        "message": message,
        "should_escalate": False,
    }


def build_knowledge_reply(item: dict | None, fallback_message: str) -> dict:
    if not item:
        return {
            "reply_type": "knowledge_not_found",
            "message": fallback_message,
            "should_escalate": True,
        }

    content = item.get("content", {})
    message = content.get("message")

    if not message:
        return {
            "reply_type": "knowledge_incomplete",
            "message": fallback_message,
            "should_escalate": True,
        }

    return {
        "reply_type": "knowledge_reply",
        "message": message,
        "should_escalate": False,
    }