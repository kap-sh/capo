"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceCriticality``."""

from typing import Literal, TypeAlias, cast

ResourceCriticality: TypeAlias = Literal[
    "Very High",
    "High",
    "Medium",
    "Low",
    "Unknown",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCriticality) -> str:
    return value


def deserialize_json(data: str) -> ResourceCriticality:
    return cast(ResourceCriticality, data)
