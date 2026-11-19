"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotMode``."""

from typing import Literal, TypeAlias, cast

SnapshotMode: TypeAlias = Literal[
    "APPLICATION_SNAPSHOTS_LEGACY",
    "ENHANCED_SNAPSHOTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotMode:
    return cast(SnapshotMode, data)
