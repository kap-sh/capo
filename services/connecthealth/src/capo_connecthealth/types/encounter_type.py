"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncounterType``."""

from typing import Literal, TypeAlias, cast

EncounterType: TypeAlias = Literal[
    "TELEHEALTH",
    "IN_PERSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncounterType) -> str:
    return value


def deserialize_json(data: str) -> EncounterType:
    return cast(EncounterType, data)
