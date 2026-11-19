"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayPrivateIpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string

NatGatewayPrivateIpList: TypeAlias = list[
    "capo_network_firewall.types.collection_member_string.CollectionMember_String"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayPrivateIpList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NatGatewayPrivateIpList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NatGatewayPrivateIpList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> NatGatewayPrivateIpList:
    return [item for item in data if item is not None]
