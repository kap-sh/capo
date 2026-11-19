"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Firewalls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_metadata

Firewalls: TypeAlias = list[
    "capo_network_firewall.types.firewall_metadata.FirewallMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Firewalls) -> list:
    import capo_network_firewall.types.firewall_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_metadata.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Firewalls:
    import capo_network_firewall.types.firewall_metadata

    out: Firewalls = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_metadata.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Firewalls) -> list:
    import capo_network_firewall.types.firewall_metadata

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.firewall_metadata.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Firewalls:
    import capo_network_firewall.types.firewall_metadata

    out: Firewalls = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.firewall_metadata.deserialize_cbor(item))
    return out
