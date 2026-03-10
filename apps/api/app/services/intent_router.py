import unicodedata


def normalize_text(text: str) -> str:
    text = text.strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    return text


def detect_intent(text: str | None) -> str:
    if not text:
        return "unknown"

    normalized = normalize_text(text)

    if normalized.startswith("track "):
        return "tracking_lookup"

    if "tarif" in normalized or "rate" in normalized or "price" in normalized:
        return "pricing_query"

    if (
        "adresse" in normalized
        or "address" in normalized
        or "entrepot" in normalized
        or "warehouse" in normalized
    ):
        return "warehouse_address"

    if "depart" in normalized or "departure" in normalized:
        return "departure_query"

    return "unknown"