"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationPriority``."""

from typing import Literal, TypeAlias, cast

RemediationPriority: TypeAlias = Literal[
    "Critical",
    "High",
    "Medium",
    "Low",
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationPriority) -> str:
    return value


def deserialize_json(data: str) -> RemediationPriority:
    return cast(RemediationPriority, data)
