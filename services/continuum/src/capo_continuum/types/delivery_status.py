"""Generated from Smithy shape ``com.amazonaws.continuum#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

DeliveryStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
    "SKIPPED",
    "ABANDONED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliveryStatus:
    return cast(DeliveryStatus, data)
