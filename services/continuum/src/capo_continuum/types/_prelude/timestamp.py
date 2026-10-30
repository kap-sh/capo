"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime


# --- restJson1 ser/de ---
def serialize_json(value: datetime.datetime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
