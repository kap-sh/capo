"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeType``."""

from typing import Literal, TypeAlias, cast

ComputeType: TypeAlias = Literal[
    "EC2",
    "ANYWHERE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeType:
    return cast(ComputeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeType) -> str:
    return value


def deserialize_cbor(data: str) -> ComputeType:
    return cast(ComputeType, data)
