"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FabricSwitchingMode``."""

from typing import Literal, TypeAlias, cast

FabricSwitchingMode: TypeAlias = Literal[
    "IMMEDIATE",
    "KEY_FRAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: FabricSwitchingMode) -> str:
    return value


def deserialize_json(data: str) -> FabricSwitchingMode:
    return cast(FabricSwitchingMode, data)
