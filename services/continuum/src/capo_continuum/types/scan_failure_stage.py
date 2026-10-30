"""Generated from Smithy shape ``com.amazonaws.continuum#ScanFailureStage``."""

from typing import Literal, TypeAlias, cast

"""The phase a failed scan was in when it failed. Present only on a FAILED scan, and absent on one that failed before this field existed. Shares its vocabulary with the non-terminal ScanStatus values so a failure reads directly against the phase sequence, with no mapping."""
ScanFailureStage: TypeAlias = Literal[
    "SUBMITTED",
    "WAITING_FOR_BUILD",
    "BUILDING",
    "WAITING_FOR_SCAN",
    "SCANNING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanFailureStage) -> str:
    return value


def deserialize_json(data: str) -> ScanFailureStage:
    return cast(ScanFailureStage, data)
