"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.tcp_flag

Flags: TypeAlias = list["capo_network_firewall.types.tcp_flag.TCPFlag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flags) -> list:
    import capo_network_firewall.types.tcp_flag

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.tcp_flag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Flags:
    import capo_network_firewall.types.tcp_flag

    out: Flags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.tcp_flag.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Flags) -> list:
    import capo_network_firewall.types.tcp_flag

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.tcp_flag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Flags:
    import capo_network_firewall.types.tcp_flag

    out: Flags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.tcp_flag.deserialize_cbor(item))
    return out
