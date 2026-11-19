"""Generated from Smithy shape ``com.amazonaws.health#DescribeEntityAggregatesTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

DescribeEntityAggregatesTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityAggregatesTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeEntityAggregatesTagValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEntityAggregatesTagValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DescribeEntityAggregatesTagValueList:
    return [item for item in data if item is not None]
