"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilterName``."""

from typing import Literal, TypeAlias, cast

TargetFilterName: TypeAlias = Literal["TARGET_STATUS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetFilterName:
    return cast(TargetFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> TargetFilterName:
    return cast(TargetFilterName, data)
