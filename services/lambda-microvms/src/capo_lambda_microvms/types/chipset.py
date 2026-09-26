"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#Chipset``."""

from typing import Literal, TypeAlias, cast

Chipset: TypeAlias = Literal["GRAVITON",]


# --- restJson1 ser/de ---
def serialize_json(value: Chipset) -> str:
    return value


def deserialize_json(data: str) -> Chipset:
    return cast(Chipset, data)
