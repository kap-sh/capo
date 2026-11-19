"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GroupByAttribute``."""

from typing import Literal, TypeAlias, cast

GroupByAttribute: TypeAlias = Literal[
    "TARGET_ID",
    "REGION",
    "RESOURCE_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupByAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupByAttribute:
    return cast(GroupByAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GroupByAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> GroupByAttribute:
    return cast(GroupByAttribute, data)
