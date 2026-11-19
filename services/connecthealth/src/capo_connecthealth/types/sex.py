"""Generated from Smithy shape ``com.amazonaws.connecthealth#Sex``."""

from typing import Literal, TypeAlias, cast

Sex: TypeAlias = Literal[
    "MALE",
    "FEMALE",
    "NON_BINARY",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: Sex) -> str:
    return value


def deserialize_json(data: str) -> Sex:
    return cast(Sex, data)
