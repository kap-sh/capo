"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TargetIdType``."""

from typing import Literal, TypeAlias, cast

TargetIdType: TypeAlias = Literal[
    "ACCOUNT",
    "OU",
    "ROOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetIdType:
    return cast(TargetIdType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetIdType) -> str:
    return value


def deserialize_cbor(data: str) -> TargetIdType:
    return cast(TargetIdType, data)
