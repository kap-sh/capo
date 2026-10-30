"""Generated from Smithy shape ``com.amazonaws.continuum#IssuePatchDeliveryStatus``."""

from typing import Literal, TypeAlias, cast

"""Overall customer delivery result of an issue's patches."""
IssuePatchDeliveryStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssuePatchDeliveryStatus) -> str:
    return value


def deserialize_json(data: str) -> IssuePatchDeliveryStatus:
    return cast(IssuePatchDeliveryStatus, data)
