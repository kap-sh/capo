"""Generated from Smithy shape ``com.amazonaws.endusermessaging#CodeType``."""

from typing import Literal, TypeAlias, cast

"""OTP character alphabet used by a NotifyCodeConfiguration."""
CodeType: TypeAlias = Literal[
    "NUMERIC",
    "ALPHA",
    "ALPHANUMERIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeType) -> str:
    return value


def deserialize_json(data: str) -> CodeType:
    return cast(CodeType, data)
