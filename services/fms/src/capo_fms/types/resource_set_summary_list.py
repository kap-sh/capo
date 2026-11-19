"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource_set_summary

ResourceSetSummaryList: TypeAlias = list[
    "capo_fms.types.resource_set_summary.ResourceSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetSummaryList) -> list:
    import capo_fms.types.resource_set_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource_set_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceSetSummaryList:
    import capo_fms.types.resource_set_summary

    out: ResourceSetSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource_set_summary.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceSetSummaryList) -> list:
    import capo_fms.types.resource_set_summary

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource_set_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceSetSummaryList:
    import capo_fms.types.resource_set_summary

    out: ResourceSetSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource_set_summary.deserialize_cbor(item))
    return out
