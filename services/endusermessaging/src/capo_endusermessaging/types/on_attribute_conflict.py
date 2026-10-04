"""Generated from Smithy shape ``com.amazonaws.endusermessaging#OnAttributeConflict``."""

from typing import Literal, TypeAlias, cast

"""Strategy for merging registration data into brand profile attributes."""
OnAttributeConflict: TypeAlias = Literal[
    "REPLACE",
    "PRESERVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnAttributeConflict) -> str:
    return value


def deserialize_json(data: str) -> OnAttributeConflict:
    return cast(OnAttributeConflict, data)
