"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#SummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.summary

SummaryList: TypeAlias = list["capo_resource_groups_tagging_api.types.summary.Summary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummaryList) -> list:
    import capo_resource_groups_tagging_api.types.summary

    out: list = []
    for item in value:
        out.append(
            capo_resource_groups_tagging_api.types.summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SummaryList:
    import capo_resource_groups_tagging_api.types.summary

    out: SummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummaryList) -> list:
    import capo_resource_groups_tagging_api.types.summary

    out: list = []
    for item in value:
        out.append(capo_resource_groups_tagging_api.types.summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SummaryList:
    import capo_resource_groups_tagging_api.types.summary

    out: SummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_resource_groups_tagging_api.types.summary.deserialize_cbor(item)
        )
    return out
