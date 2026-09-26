"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoDetectionScope``."""

from typing import Literal, TypeAlias, cast

AutoDetectionScope: TypeAlias = Literal["ORGANIZATION",]


# --- restJson1 ser/de ---
def serialize_json(value: AutoDetectionScope) -> str:
    return value


def deserialize_json(data: str) -> AutoDetectionScope:
    return cast(AutoDetectionScope, data)
