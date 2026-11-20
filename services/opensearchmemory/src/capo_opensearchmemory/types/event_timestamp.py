"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EventTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>The time of an event or memory.</p>"""
EventTimestamp: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_aws_json_1_0(data: str) -> EventTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
