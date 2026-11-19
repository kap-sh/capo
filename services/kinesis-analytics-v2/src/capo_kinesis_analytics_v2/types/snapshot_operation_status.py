"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationStatus``."""

from typing import Literal, TypeAlias, cast

SnapshotOperationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotOperationStatus:
    return cast(SnapshotOperationStatus, data)
