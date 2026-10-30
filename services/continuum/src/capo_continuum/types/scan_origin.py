"""Generated from Smithy shape ``com.amazonaws.continuum#ScanOrigin``."""

from typing import Literal, TypeAlias, cast

"""Identifies why a scan run was created."""
ScanOrigin: TypeAlias = Literal[
    "MANUAL",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanOrigin) -> str:
    return value


def deserialize_json(data: str) -> ScanOrigin:
    return cast(ScanOrigin, data)
