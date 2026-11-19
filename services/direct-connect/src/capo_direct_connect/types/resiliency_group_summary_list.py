"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.resiliency_group_summary

ResiliencyGroupSummaryList: TypeAlias = list[
    "capo_direct_connect.types.resiliency_group_summary.ResiliencyGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupSummaryList) -> list:
    import capo_direct_connect.types.resiliency_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.resiliency_group_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResiliencyGroupSummaryList:
    import capo_direct_connect.types.resiliency_group_summary

    out: ResiliencyGroupSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.resiliency_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupSummaryList) -> list:
    import capo_direct_connect.types.resiliency_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.resiliency_group_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ResiliencyGroupSummaryList:
    import capo_direct_connect.types.resiliency_group_summary

    out: ResiliencyGroupSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.resiliency_group_summary.deserialize_cbor(item)
        )
    return out
