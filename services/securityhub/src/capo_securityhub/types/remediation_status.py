"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationStatus``."""

from typing import Literal, TypeAlias, cast

RemediationStatus: TypeAlias = Literal[
    "New",
    "Updated",
    "Resolved",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationStatus) -> str:
    return value


def deserialize_json(data: str) -> RemediationStatus:
    return cast(RemediationStatus, data)
