"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.tag_filter

TagFilterList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.tag_filter.TagFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilterList) -> list:
    import capo_resource_groups_tagging_api.types.tag_filter

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.tag_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagFilterList:
    import capo_resource_groups_tagging_api.types.tag_filter

    out: TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.tag_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagFilterList) -> list:
    import capo_resource_groups_tagging_api.types.tag_filter

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.tag_filter.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> TagFilterList:
    import capo_resource_groups_tagging_api.types.tag_filter

    out: TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.tag_filter.deserialize_cbor(item)
        )
    return out
