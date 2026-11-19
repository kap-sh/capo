"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GroupBy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.group_by_attribute

GroupBy: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.group_by_attribute.GroupByAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupBy) -> list:
    import capo_resource_groups_tagging_api.types.group_by_attribute

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.group_by_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupBy:
    import capo_resource_groups_tagging_api.types.group_by_attribute

    out: GroupBy = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.group_by_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GroupBy) -> list:
    import capo_resource_groups_tagging_api.types.group_by_attribute

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.group_by_attribute.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> GroupBy:
    import capo_resource_groups_tagging_api.types.group_by_attribute

    out: GroupBy = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.group_by_attribute.deserialize_cbor(
                item
            )
        )
    return out
