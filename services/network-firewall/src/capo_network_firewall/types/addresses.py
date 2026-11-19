"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.address

Addresses: TypeAlias = list["capo_network_firewall.types.address.Address"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Addresses) -> list:
    import capo_network_firewall.types.address

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.address.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Addresses:
    import capo_network_firewall.types.address

    out: Addresses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.address.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Addresses) -> list:
    import capo_network_firewall.types.address

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.address.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Addresses:
    import capo_network_firewall.types.address

    out: Addresses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.address.deserialize_cbor(item))
    return out
