"""Generated from Smithy shape ``com.amazonaws.endusermessaging#VoiceMessageBodyTextType``."""

from typing import Literal, TypeAlias, cast

"""The format of the voice message body text."""
VoiceMessageBodyTextType: TypeAlias = Literal[
    "TEXT",
    "SSML",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceMessageBodyTextType) -> str:
    return value


def deserialize_json(data: str) -> VoiceMessageBodyTextType:
    return cast(VoiceMessageBodyTextType, data)
