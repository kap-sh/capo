"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.vpc_id

VpcIds: TypeAlias = list["capo_network_firewall.types.vpc_id.VpcId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VpcIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VpcIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> VpcIds:
    return [item for item in data if item is not None]
