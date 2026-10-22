"""Generated from Smithy shape ``com.amazonaws.datazone#UserDesignation``."""

from typing import Literal, TypeAlias, cast

UserDesignation: TypeAlias = Literal[
    "PROJECT_OWNER",
    "PROJECT_CONTRIBUTOR",
    "PROJECT_CATALOG_VIEWER",
    "PROJECT_CATALOG_CONSUMER",
    "PROJECT_CATALOG_STEWARD",
    "USER_CREATED_DESIGNATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserDesignation) -> str:
    return value


def deserialize_json(data: str) -> UserDesignation:
    return cast(UserDesignation, data)
