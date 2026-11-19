"""Generated from Smithy shape ``com.amazonaws.securityagent#ErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Error code for pentest job failure.</p>"""
ErrorCode: TypeAlias = Literal[
    "CLIENT_ERROR",
    "INTERNAL_ERROR",
    "STOPPED_BY_USER",
    "PAUSED_BY_USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
