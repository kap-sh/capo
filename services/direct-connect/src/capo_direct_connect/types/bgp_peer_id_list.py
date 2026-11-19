"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer_id

BGPPeerIdList: TypeAlias = list["capo_direct_connect.types.bgp_peer_id.BGPPeerId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeerIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BGPPeerIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BGPPeerIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> BGPPeerIdList:
    return [item for item in data if item is not None]
