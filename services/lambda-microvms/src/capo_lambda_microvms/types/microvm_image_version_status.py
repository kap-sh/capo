"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmImageVersionStatus``."""

from typing import Literal, TypeAlias, cast

MicrovmImageVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmImageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> MicrovmImageVersionStatus:
    return cast(MicrovmImageVersionStatus, data)
