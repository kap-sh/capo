"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProtocolStrings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.protocol_string

ProtocolStrings: TypeAlias = list[
    "capo_network_firewall.types.protocol_string.ProtocolString"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtocolStrings) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProtocolStrings:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolStrings) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtocolStrings:
    return [item for item in data if item is not None]
