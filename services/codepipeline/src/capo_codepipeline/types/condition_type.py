"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionType``."""

from typing import Literal, TypeAlias, cast

ConditionType: TypeAlias = Literal[
    "BEFORE_ENTRY",
    "ON_SUCCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionType:
    return cast(ConditionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionType) -> str:
    return value


def deserialize_cbor(data: str) -> ConditionType:
    return cast(ConditionType, data)
