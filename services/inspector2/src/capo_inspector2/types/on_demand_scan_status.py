"""Generated from Smithy shape ``com.amazonaws.inspector2#OnDemandScanStatus``."""

from typing import Literal, TypeAlias, cast

OnDemandScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnDemandScanStatus) -> str:
    return value


def deserialize_json(data: str) -> OnDemandScanStatus:
    return cast(OnDemandScanStatus, data)
