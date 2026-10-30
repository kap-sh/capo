"""Generated from Smithy shape ``com.amazonaws.opensearch#DiffStatus``."""

from typing import Literal, TypeAlias, cast

DiffStatus: TypeAlias = Literal[
    "compared",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiffStatus) -> str:
    return value


def deserialize_json(data: str) -> DiffStatus:
    return cast(DiffStatus, data)
