"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillResultStatus``."""

from typing import Literal, TypeAlias, cast

ReplicationBackfillResultStatus: TypeAlias = Literal[
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillResultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationBackfillResultStatus:
    return cast(ReplicationBackfillResultStatus, data)
