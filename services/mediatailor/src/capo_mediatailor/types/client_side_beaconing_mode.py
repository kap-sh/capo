"""Generated from Smithy shape ``com.amazonaws.mediatailor#ClientSideBeaconingMode``."""

from typing import Literal, TypeAlias, cast

ClientSideBeaconingMode: TypeAlias = Literal[
    "DISABLED",
    "INSIGHTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientSideBeaconingMode) -> str:
    return value


def deserialize_json(data: str) -> ClientSideBeaconingMode:
    return cast(ClientSideBeaconingMode, data)
