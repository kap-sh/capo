"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotInitiator``."""

from typing import Literal, TypeAlias, cast

SnapshotInitiator: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotInitiator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotInitiator:
    return cast(SnapshotInitiator, data)
