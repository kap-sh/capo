"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PortRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.port_range

PortRanges: TypeAlias = list["capo_network_firewall.types.port_range.PortRange"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PortRanges) -> list:
    import capo_network_firewall.types.port_range

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.port_range.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PortRanges:
    import capo_network_firewall.types.port_range

    out: PortRanges = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.port_range.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PortRanges) -> list:
    import capo_network_firewall.types.port_range

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.port_range.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PortRanges:
    import capo_network_firewall.types.port_range

    out: PortRanges = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.port_range.deserialize_cbor(item))
    return out
