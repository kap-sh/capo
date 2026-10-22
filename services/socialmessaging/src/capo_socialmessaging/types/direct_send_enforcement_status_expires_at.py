"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DirectSendEnforcementStatusExpiresAt``."""

import datetime
from typing import TypeAlias

DirectSendEnforcementStatusExpiresAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DirectSendEnforcementStatusExpiresAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DirectSendEnforcementStatusExpiresAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
