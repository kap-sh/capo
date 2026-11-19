"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedEntitiesTagValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.tag_filter_value

DescribeAffectedEntitiesTagValueList: TypeAlias = list[
    "capo_health.types.tag_filter_value.TagFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAffectedEntitiesTagValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeAffectedEntitiesTagValueList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAffectedEntitiesTagValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DescribeAffectedEntitiesTagValueList:
    return [item for item in data if item is not None]
