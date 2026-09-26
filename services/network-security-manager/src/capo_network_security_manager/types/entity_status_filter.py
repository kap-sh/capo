"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#EntityStatusFilter``."""

from typing import Literal, TypeAlias, cast

EntityStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "DRAFT",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityStatusFilter) -> str:
    return value


def deserialize_json(data: str) -> EntityStatusFilter:
    return cast(EntityStatusFilter, data)
