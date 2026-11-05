"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationState``."""

from typing import Literal, TypeAlias, cast

MigrationState: TypeAlias = Literal[
    "new",
    "planning",
    "pendingReview",
    "queued",
    "migrating",
    "succeeded",
    "failed",
    "cancelling",
    "cancelled",
]


# --- restJson1 ser/de ---
def serialize_json(value: MigrationState) -> str:
    return value


def deserialize_json(data: str) -> MigrationState:
    return cast(MigrationState, data)
