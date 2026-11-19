"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStatus``."""

from typing import Literal, TypeAlias, cast

QueueStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueueStatus:
    return cast(QueueStatus, data)
