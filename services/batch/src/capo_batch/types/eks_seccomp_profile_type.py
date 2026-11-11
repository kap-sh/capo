"""Generated from Smithy shape ``com.amazonaws.batch#EksSeccompProfileType``."""

from typing import Literal, TypeAlias, cast

EksSeccompProfileType: TypeAlias = Literal[
    "RuntimeDefault",
    "Localhost",
    "Unconfined",
]


# --- restJson1 ser/de ---
def serialize_json(value: EksSeccompProfileType) -> str:
    return value


def deserialize_json(data: str) -> EksSeccompProfileType:
    return cast(EksSeccompProfileType, data)
