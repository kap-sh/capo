"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.namespace_summary

NamespaceSummariesList: TypeAlias = list[
    "capo_servicediscovery.types.namespace_summary.NamespaceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceSummariesList) -> list:
    import capo_servicediscovery.types.namespace_summary

    out: list = []
    for item in value:
        out.append(
            capo_servicediscovery.types.namespace_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NamespaceSummariesList:
    import capo_servicediscovery.types.namespace_summary

    out: NamespaceSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_servicediscovery.types.namespace_summary.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NamespaceSummariesList) -> list:
    import capo_servicediscovery.types.namespace_summary

    out: list = []
    for item in value:
        out.append(capo_servicediscovery.types.namespace_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NamespaceSummariesList:
    import capo_servicediscovery.types.namespace_summary

    out: NamespaceSummariesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_servicediscovery.types.namespace_summary.deserialize_cbor(item))
    return out
