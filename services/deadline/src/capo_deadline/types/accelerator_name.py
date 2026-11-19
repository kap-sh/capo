"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorName``."""

from typing import Literal, TypeAlias, cast

AcceleratorName: TypeAlias = Literal[
    "t4",
    "a10g",
    "l4",
    "l40s",
    "rtx-pro-server-6000",
    "rtx-pro-4500",
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorName) -> str:
    return value


def deserialize_json(data: str) -> AcceleratorName:
    return cast(AcceleratorName, data)
