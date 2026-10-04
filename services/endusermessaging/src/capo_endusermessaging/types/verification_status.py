"""Generated from Smithy shape ``com.amazonaws.endusermessaging#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

"""Outcome of a ValidateNotifyCodeVerification request."""
VerificationStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerificationStatus) -> str:
    return value


def deserialize_json(data: str) -> VerificationStatus:
    return cast(VerificationStatus, data)
