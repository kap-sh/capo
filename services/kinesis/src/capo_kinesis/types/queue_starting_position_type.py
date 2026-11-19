"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStartingPositionType``."""

from typing import Literal, TypeAlias, cast

QueueStartingPositionType: TypeAlias = Literal[
    "TRIM_HORIZON",
    "LATEST",
    "AT_TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStartingPositionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueueStartingPositionType:
    return cast(QueueStartingPositionType, data)
