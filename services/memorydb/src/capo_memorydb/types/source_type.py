"""Generated from Smithy shape ``com.amazonaws.memorydb#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "node",
    "parameter-group",
    "subnet-group",
    "cluster",
    "user",
    "acl",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    return cast(SourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceType) -> str:
    return value


def deserialize_cbor(data: str) -> SourceType:
    return cast(SourceType, data)
