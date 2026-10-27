"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationBackfillStatus: TypeAlias = Literal[
    "PREPARING",
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationBackfillStatus:
    return cast(ReplicationBackfillStatus, data)
