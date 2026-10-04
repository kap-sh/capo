"""Generated from Smithy shape ``com.amazonaws.ssm#DeletionMode``."""

from typing import Literal, TypeAlias, cast

DeletionMode: TypeAlias = Literal[
    "RemoveSharing",
    "RollbackMigration",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletionMode:
    return cast(DeletionMode, data)
