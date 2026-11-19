"""Generated from Smithy shape ``com.amazonaws.connecthealth#PatientStatus``."""

from typing import Literal, TypeAlias, cast

PatientStatus: TypeAlias = Literal[
    "NEW",
    "ESTABLISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PatientStatus) -> str:
    return value


def deserialize_json(data: str) -> PatientStatus:
    return cast(PatientStatus, data)
