"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.dimension

Dimensions: TypeAlias = list["capo_network_firewall.types.dimension.Dimension"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimensions) -> list:
    import capo_network_firewall.types.dimension

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.dimension.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Dimensions:
    import capo_network_firewall.types.dimension

    out: Dimensions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.dimension.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Dimensions) -> list:
    import capo_network_firewall.types.dimension

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.dimension.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Dimensions:
    import capo_network_firewall.types.dimension

    out: Dimensions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.dimension.deserialize_cbor(item))
    return out
