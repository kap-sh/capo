"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ScopeCoverageStatus``."""

from typing import Literal, TypeAlias, cast

ScopeCoverageStatus: TypeAlias = Literal[
    "COMPLETE",
    "INCOMPLETE",
    "PENDING",
    "STALE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeCoverageStatus) -> str:
    return value


def deserialize_json(data: str) -> ScopeCoverageStatus:
    return cast(ScopeCoverageStatus, data)
