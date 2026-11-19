"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AzSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.az_subnet

AzSubnets: TypeAlias = list["capo_network_firewall.types.az_subnet.AzSubnet"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AzSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AzSubnets:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AzSubnets) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AzSubnets:
    return [item for item in data if item is not None]
