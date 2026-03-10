import re


TRACKING_PATTERN = re.compile(r"\bTRACK\s+([A-Za-z0-9\-]+)\b", re.IGNORECASE)


def extract_tracking_id(text: str | None) -> str | None:
    if not text:
        return None

    match = TRACKING_PATTERN.search(text.strip())
    if not match:
        return None

    return match.group(1)