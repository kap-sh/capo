"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteType``."""

from typing import Literal, TypeAlias, cast

RouteType: TypeAlias = Literal[
    "PROPAGATED",
    "STATIC",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteType) -> str:
    return value


def deserialize_json(data: str) -> RouteType:
    return cast(RouteType, data)
