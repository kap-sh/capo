"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#EntityStatus``."""

from typing import Literal, TypeAlias, cast

EntityStatus: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityStatus) -> str:
    return value


def deserialize_json(data: str) -> EntityStatus:
    return cast(EntityStatus, data)
