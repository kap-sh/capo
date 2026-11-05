"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationRequestedState``."""

from typing import Literal, TypeAlias, cast

MigrationRequestedState: TypeAlias = Literal[
    "queued",
    "cancelled",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationRequestedState) -> str:
    return value


def deserialize_json(data: str) -> MigrationRequestedState:
    return cast(MigrationRequestedState, data)
