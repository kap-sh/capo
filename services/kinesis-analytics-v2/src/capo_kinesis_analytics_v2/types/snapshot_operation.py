"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperation``."""

from typing import Literal, TypeAlias, cast

SnapshotOperation: TypeAlias = Literal[
    "CreateSnapshot",
    "DeleteSnapshot",
    "ImportSnapshot",
    "ExportSnapshot",
    "SystemCreateSnapshot",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotOperation:
    return cast(SnapshotOperation, data)
