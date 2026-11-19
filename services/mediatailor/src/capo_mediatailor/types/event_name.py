"""Generated from Smithy shape ``com.amazonaws.mediatailor#EventName``."""

from typing import Literal, TypeAlias, cast

EventName: TypeAlias = Literal[
    "PRE_SESSION_INITIALIZATION",
    "PRE_ADS_REQUEST",
    "POST_ADS_RESPONSE",
    "PRE_MANIFEST_INSERTION",
    "POST_ORIGIN_RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventName) -> str:
    return value


def deserialize_json(data: str) -> EventName:
    return cast(EventName, data)
