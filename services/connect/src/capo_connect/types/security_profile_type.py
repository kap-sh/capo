"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileType``."""

from typing import Literal, TypeAlias, cast

SecurityProfileType: TypeAlias = Literal[
    "AWS_MANAGED",
    "CUSTOMER_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileType) -> str:
    return value


def deserialize_json(data: str) -> SecurityProfileType:
    return cast(SecurityProfileType, data)
