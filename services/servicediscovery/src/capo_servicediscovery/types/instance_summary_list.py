"""Generated from Smithy shape ``com.amazonaws.servicediscovery#InstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.instance_summary

InstanceSummaryList: TypeAlias = list[
    "capo_servicediscovery.types.instance_summary.InstanceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSummaryList) -> list:
    import capo_servicediscovery.types.instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_servicediscovery.types.instance_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceSummaryList:
    import capo_servicediscovery.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_servicediscovery.types.instance_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceSummaryList) -> list:
    import capo_servicediscovery.types.instance_summary

    out: list = []
    for item in value:
        out.append(capo_servicediscovery.types.instance_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> InstanceSummaryList:
    import capo_servicediscovery.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_servicediscovery.types.instance_summary.deserialize_cbor(item))
    return out
