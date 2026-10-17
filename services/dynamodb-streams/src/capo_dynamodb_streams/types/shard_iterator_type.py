"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ShardIteratorType``."""

from typing import Literal, TypeAlias, cast

ShardIteratorType: TypeAlias = Literal[
    "TRIM_HORIZON",
    "LATEST",
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShardIteratorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShardIteratorType:
    return cast(ShardIteratorType, data)
