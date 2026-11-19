"""Generated from Smithy shape ``com.amazonaws.lambda#AcceleratorMemoryGB``."""

from typing import Literal, TypeAlias, cast

AcceleratorMemoryGB: TypeAlias = Literal[
    3,
    6,
    12,
    16,
    24,
    48,
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorMemoryGB) -> int:
    return value


def deserialize_json(data: int) -> AcceleratorMemoryGB:
    return cast(AcceleratorMemoryGB, data)
