"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SubnetMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.subnet_mapping

SubnetMappings: TypeAlias = list[
    "capo_network_firewall.types.subnet_mapping.SubnetMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetMappings) -> list:
    import capo_network_firewall.types.subnet_mapping

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.subnet_mapping.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SubnetMappings:
    import capo_network_firewall.types.subnet_mapping

    out: SubnetMappings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.subnet_mapping.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubnetMappings) -> list:
    import capo_network_firewall.types.subnet_mapping

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.subnet_mapping.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SubnetMappings:
    import capo_network_firewall.types.subnet_mapping

    out: SubnetMappings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.subnet_mapping.deserialize_cbor(item))
    return out
