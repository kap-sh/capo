"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyChannel``."""

from typing import Literal, TypeAlias, cast

"""Channel used to deliver an OTP to the end user."""
NotifyChannel: TypeAlias = Literal[
    "TEXT",
    "VOICE",
    "WHATSAPP",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyChannel) -> str:
    return value


def deserialize_json(data: str) -> NotifyChannel:
    return cast(NotifyChannel, data)
