"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotFormat``."""

from typing import Literal, TypeAlias, cast

SnapshotFormat: TypeAlias = Literal["CANONICAL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotFormat:
    return cast(SnapshotFormat, data)
