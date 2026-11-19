"""Generated from Smithy shape ``com.amazonaws.codedeploy#EC2TagFilterType``."""

from typing import Literal, TypeAlias, cast

EC2TagFilterType: TypeAlias = Literal[
    "KEY_ONLY",
    "VALUE_ONLY",
    "KEY_AND_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2TagFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EC2TagFilterType:
    return cast(EC2TagFilterType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EC2TagFilterType) -> str:
    return value


def deserialize_cbor(data: str) -> EC2TagFilterType:
    return cast(EC2TagFilterType, data)
