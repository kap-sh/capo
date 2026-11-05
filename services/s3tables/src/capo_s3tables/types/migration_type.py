"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationType``."""

from typing import Literal, TypeAlias, cast

MigrationType: TypeAlias = Literal[
    "start",
    "sync",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationType) -> str:
    return value


def deserialize_json(data: str) -> MigrationType:
    return cast(MigrationType, data)
