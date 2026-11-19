"""Generated from Smithy shape ``com.amazonaws.elementalinference#FrameSamplingMode``."""

from typing import Literal, TypeAlias, cast

FrameSamplingMode: TypeAlias = Literal[
    "FIRST",
    "UNIFORM",
    "LAST",
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameSamplingMode) -> str:
    return value


def deserialize_json(data: str) -> FrameSamplingMode:
    return cast(FrameSamplingMode, data)
