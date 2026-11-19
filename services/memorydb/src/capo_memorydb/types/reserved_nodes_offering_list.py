"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNodesOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.reserved_nodes_offering

ReservedNodesOfferingList: TypeAlias = list[
    "capo_memorydb.types.reserved_nodes_offering.ReservedNodesOffering"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNodesOfferingList) -> list:
    import capo_memorydb.types.reserved_nodes_offering

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.reserved_nodes_offering.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservedNodesOfferingList:
    import capo_memorydb.types.reserved_nodes_offering

    out: ReservedNodesOfferingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.reserved_nodes_offering.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReservedNodesOfferingList) -> list:
    import capo_memorydb.types.reserved_nodes_offering

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.reserved_nodes_offering.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ReservedNodesOfferingList:
    import capo_memorydb.types.reserved_nodes_offering

    out: ReservedNodesOfferingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.reserved_nodes_offering.deserialize_cbor(item))
    return out
