"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.hash_map_key
    import capo_network_firewall.types.hash_map_value

LogDestinationMap: TypeAlias = dict[
    "capo_network_firewall.types.hash_map_key.HashMapKey",
    "capo_network_firewall.types.hash_map_value.HashMapValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: LogDestinationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestinationMap:
    out: LogDestinationMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LogDestinationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> LogDestinationMap:
    out: LogDestinationMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
