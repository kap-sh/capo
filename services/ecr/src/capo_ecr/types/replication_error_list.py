"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.replication_error

ReplicationErrorList: TypeAlias = list[
    "capo_ecr.types.replication_error.ReplicationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationErrorList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplicationErrorList:
    return [item for item in data if item is not None]
