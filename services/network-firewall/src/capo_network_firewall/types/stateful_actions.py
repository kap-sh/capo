"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string

StatefulActions: TypeAlias = list[
    "capo_network_firewall.types.collection_member_string.CollectionMember_String"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulActions) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StatefulActions:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatefulActions) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StatefulActions:
    return [item for item in data if item is not None]
