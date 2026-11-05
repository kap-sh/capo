"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationInputFormat``."""

from typing import Literal, TypeAlias, cast

BulkOperationInputFormat: TypeAlias = Literal[
    "DYNAMODB_JSON",
    "ION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationInputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BulkOperationInputFormat:
    return cast(BulkOperationInputFormat, data)
