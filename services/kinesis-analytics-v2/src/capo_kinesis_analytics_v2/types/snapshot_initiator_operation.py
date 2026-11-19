"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotInitiatorOperation``."""

from typing import Literal, TypeAlias, cast

SnapshotInitiatorOperation: TypeAlias = Literal[
    "CreateSnapshot",
    "ImportSnapshot",
    "SystemCreateSnapshot",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotInitiatorOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotInitiatorOperation:
    return cast(SnapshotInitiatorOperation, data)
