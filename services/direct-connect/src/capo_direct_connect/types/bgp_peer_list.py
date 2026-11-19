"""Generated from Smithy shape ``com.amazonaws.directconnect#BGPPeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.bgp_peer

BGPPeerList: TypeAlias = list["capo_direct_connect.types.bgp_peer.BGPPeer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BGPPeerList) -> list:
    import capo_direct_connect.types.bgp_peer

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.bgp_peer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BGPPeerList:
    import capo_direct_connect.types.bgp_peer

    out: BGPPeerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.bgp_peer.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BGPPeerList) -> list:
    import capo_direct_connect.types.bgp_peer

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.bgp_peer.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BGPPeerList:
    import capo_direct_connect.types.bgp_peer

    out: BGPPeerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.bgp_peer.deserialize_cbor(item))
    return out
