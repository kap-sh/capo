"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchType``."""

from typing import Literal, TypeAlias, cast

FetchType: TypeAlias = Literal[
    "FINDINGS",
    "DETECTOR",
    "REPUTATION",
    "FINDING_TYPE_DOCUMENTATION",
    "CLOUD_TRAIL_RAW_EVENTS",
    "RUNTIME_SIGNALS",
    "MEMBER_ACCOUNTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchType) -> str:
    return value


def deserialize_json(data: str) -> FetchType:
    return cast(FetchType, data)
