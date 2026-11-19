"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#RequiredTagsForListRequiredTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.required_tag

RequiredTagsForListRequiredTags: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.required_tag.RequiredTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequiredTagsForListRequiredTags) -> list:
    import capo_resource_groups_tagging_api.types.required_tag

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.required_tag.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RequiredTagsForListRequiredTags:
    import capo_resource_groups_tagging_api.types.required_tag

    out: RequiredTagsForListRequiredTags = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.required_tag.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RequiredTagsForListRequiredTags) -> list:
    import capo_resource_groups_tagging_api.types.required_tag

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.required_tag.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> RequiredTagsForListRequiredTags:
    import capo_resource_groups_tagging_api.types.required_tag

    out: RequiredTagsForListRequiredTags = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.required_tag.deserialize_cbor(item)
        )
    return out
