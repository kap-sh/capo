"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateBGPPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.new_bgp_peer
    import capo_direct_connect.types.virtual_interface_id


class CreateBGPPeerRequest(TypedDict, closed=True):
    virtual_interface_id: NotRequired[
        "capo_direct_connect.types.virtual_interface_id.VirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    new_bgp_peer: NotRequired["capo_direct_connect.types.new_bgp_peer.NewBGPPeer"]
    """<p>Information about the BGP peer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBGPPeerRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "new_bgp_peer" in value:
        import capo_direct_connect.types.new_bgp_peer

        out["newBGPPeer"] = (
            capo_direct_connect.types.new_bgp_peer.serialize_aws_json_1_1(
                value["new_bgp_peer"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBGPPeerRequest:
    out: CreateBGPPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("newBGPPeer") is not None:
        import capo_direct_connect.types.new_bgp_peer

        out["new_bgp_peer"] = (
            capo_direct_connect.types.new_bgp_peer.deserialize_aws_json_1_1(
                data["newBGPPeer"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateBGPPeerRequest) -> dict:
    out: dict = {}
    if "virtual_interface_id" in value:
        out["virtualInterfaceId"] = value["virtual_interface_id"]
    if "new_bgp_peer" in value:
        import capo_direct_connect.types.new_bgp_peer

        out["newBGPPeer"] = capo_direct_connect.types.new_bgp_peer.serialize_cbor(
            value["new_bgp_peer"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateBGPPeerRequest:
    out: CreateBGPPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("virtualInterfaceId") is not None:
        out["virtual_interface_id"] = data["virtualInterfaceId"]
    if data.get("newBGPPeer") is not None:
        import capo_direct_connect.types.new_bgp_peer

        out["new_bgp_peer"] = capo_direct_connect.types.new_bgp_peer.deserialize_cbor(
            data["newBGPPeer"]
        )
    return out
