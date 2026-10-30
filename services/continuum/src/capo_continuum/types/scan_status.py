"""Generated from Smithy shape ``com.amazonaws.continuum#ScanStatus``."""

from typing import Literal, TypeAlias, cast

"""The phase of a scan. A scan always builds the selected source first and then analyzes the verified result, so the phases below span both halves of the work. These values are labels, not an ordered sequence for clients to compare. A scan does not necessarily observe every phase — phases are short-lived and a poll can miss one entirely."""
ScanStatus: TypeAlias = Literal[
    "SUBMITTED",
    "WAITING_FOR_BUILD",
    "BUILDING",
    "WAITING_FOR_SCAN",
    "SCANNING",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanStatus) -> str:
    return value


def deserialize_json(data: str) -> ScanStatus:
    return cast(ScanStatus, data)
