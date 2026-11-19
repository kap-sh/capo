"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.target_filter_value

TargetFilterValueList: TypeAlias = list[
    "capo_codepipeline.types.target_filter_value.TargetFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetFilterValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetFilterValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TargetFilterValueList:
    return [item for item in data if item is not None]
