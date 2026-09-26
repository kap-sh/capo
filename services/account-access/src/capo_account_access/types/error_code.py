"""Generated from Smithy shape ``com.amazonaws.accountaccess#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "AUTHORIZATION_ERROR",
    "RESOURCE_NOT_FOUND_ERROR",
    "SERVICE_QUOTA_EXCEEDED_ERROR",
    "INTERNAL_SERVICE_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
