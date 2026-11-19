"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TCPFlags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.tcp_flag_field

TCPFlags: TypeAlias = list["capo_network_firewall.types.tcp_flag_field.TCPFlagField"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TCPFlags) -> list:
    import capo_network_firewall.types.tcp_flag_field

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.tcp_flag_field.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TCPFlags:
    import capo_network_firewall.types.tcp_flag_field

    out: TCPFlags = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.tcp_flag_field.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TCPFlags) -> list:
    import capo_network_firewall.types.tcp_flag_field

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.tcp_flag_field.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TCPFlags:
    import capo_network_firewall.types.tcp_flag_field

    out: TCPFlags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.tcp_flag_field.deserialize_cbor(item))
    return out
