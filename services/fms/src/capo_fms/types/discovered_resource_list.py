"""Generated from Smithy shape ``com.amazonaws.fms#DiscoveredResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.discovered_resource

DiscoveredResourceList: TypeAlias = list[
    "capo_fms.types.discovered_resource.DiscoveredResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResourceList) -> list:
    import capo_fms.types.discovered_resource

    out: list = []
    for item in value:
        out.append(capo_fms.types.discovered_resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DiscoveredResourceList:
    import capo_fms.types.discovered_resource

    out: DiscoveredResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.discovered_resource.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DiscoveredResourceList) -> list:
    import capo_fms.types.discovered_resource

    out: list = []
    for item in value:
        out.append(capo_fms.types.discovered_resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DiscoveredResourceList:
    import capo_fms.types.discovered_resource

    out: DiscoveredResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.discovered_resource.deserialize_cbor(item))
    return out
