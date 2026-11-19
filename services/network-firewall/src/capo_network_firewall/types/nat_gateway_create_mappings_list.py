"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayCreateMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_create_mapping

NatGatewayCreateMappingsList: TypeAlias = list[
    "capo_network_firewall.types.nat_gateway_create_mapping.NatGatewayCreateMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayCreateMappingsList) -> list:
    import capo_network_firewall.types.nat_gateway_create_mapping

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.nat_gateway_create_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NatGatewayCreateMappingsList:
    import capo_network_firewall.types.nat_gateway_create_mapping

    out: NatGatewayCreateMappingsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.nat_gateway_create_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
