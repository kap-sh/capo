"""Generated from Smithy shape ``com.amazonaws.opensearch#ReplicationRole``."""

from typing import Literal, TypeAlias, cast

ReplicationRole: TypeAlias = Literal[
    "PRIMARY",
    "SECONDARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationRole) -> str:
    return value


def deserialize_json(data: str) -> ReplicationRole:
    return cast(ReplicationRole, data)
