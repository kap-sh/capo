"""Generated from Smithy shape ``com.amazonaws.accountaccess#DateTime``."""

import datetime
from typing import TypeAlias

DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> DateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
