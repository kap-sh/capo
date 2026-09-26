"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoDetectionStatus``."""

from typing import Literal, TypeAlias, cast

AutoDetectionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoDetectionStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoDetectionStatus:
    return cast(AutoDetectionStatus, data)
