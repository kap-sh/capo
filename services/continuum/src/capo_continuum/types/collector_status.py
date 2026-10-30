"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorStatus``."""

from typing import Literal, TypeAlias, cast

"""The lifecycle status of a Collector."""
CollectorStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CollectorStatus) -> str:
    return value


def deserialize_json(data: str) -> CollectorStatus:
    return cast(CollectorStatus, data)
