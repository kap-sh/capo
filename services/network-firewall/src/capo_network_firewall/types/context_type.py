"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextType``."""

from typing import Literal, TypeAlias, cast

ContextType: TypeAlias = Literal[
    "ResourceId",
    "SegmentId",
    "Subnet",
    "Attachment",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContextType:
    return cast(ContextType, data)
