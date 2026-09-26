"""Generated from Smithy shape ``com.amazonaws.agentregistry#DateTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp in ISO 8601 date-time format</p>"""
DateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> DateTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
