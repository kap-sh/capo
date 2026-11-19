"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayAttachmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_attachment

NatGatewayAttachmentsList: TypeAlias = list[
    "capo_network_firewall.types.nat_gateway_attachment.NatGatewayAttachment"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayAttachmentsList) -> list:
    import capo_network_firewall.types.nat_gateway_attachment

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.nat_gateway_attachment.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NatGatewayAttachmentsList:
    import capo_network_firewall.types.nat_gateway_attachment

    out: NatGatewayAttachmentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.nat_gateway_attachment.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NatGatewayAttachmentsList) -> list:
    import capo_network_firewall.types.nat_gateway_attachment

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.nat_gateway_attachment.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> NatGatewayAttachmentsList:
    import capo_network_firewall.types.nat_gateway_attachment

    out: NatGatewayAttachmentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.nat_gateway_attachment.deserialize_cbor(item)
        )
    return out
