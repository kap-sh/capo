"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectMetadata``."""

from typing import Literal, TypeAlias, cast

ObjectMetadata: TypeAlias = Literal[
    "PRESERVE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectMetadata) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectMetadata:
    return cast(ObjectMetadata, data)
