"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProtocolNumbers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.protocol_number

ProtocolNumbers: TypeAlias = list[
    "capo_network_firewall.types.protocol_number.ProtocolNumber"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtocolNumbers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProtocolNumbers:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolNumbers) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtocolNumbers:
    return [item for item in data if item is not None]
