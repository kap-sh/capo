"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceTagMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.resource_tag_mapping

ResourceTagMappingList: TypeAlias = list[
    "capo_resource_groups_tagging_api.types.resource_tag_mapping.ResourceTagMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagMappingList) -> list:
    import capo_resource_groups_tagging_api.types.resource_tag_mapping

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.resource_tag_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceTagMappingList:
    import capo_resource_groups_tagging_api.types.resource_tag_mapping

    out: ResourceTagMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.resource_tag_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceTagMappingList) -> list:
    import capo_resource_groups_tagging_api.types.resource_tag_mapping

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.resource_tag_mapping.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ResourceTagMappingList:
    import capo_resource_groups_tagging_api.types.resource_tag_mapping

    out: ResourceTagMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.resource_tag_mapping.deserialize_cbor(
                item
            )
        )
    return out
