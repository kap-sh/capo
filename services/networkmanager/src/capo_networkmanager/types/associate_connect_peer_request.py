"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_id
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id


class AssociateConnectPeerRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of your global network.</p>"""
    connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId"
    """<p>The ID of the Connect peer.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateConnectPeerRequest) -> dict:
    out: dict = {}
    out["ConnectPeerId"] = value["connect_peer_id"]
    out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateConnectPeerRequest:
    out: AssociateConnectPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectPeerId") is not None:
        out["connect_peer_id"] = data["ConnectPeerId"]
    else:
        out["connect_peer_id"] = ""
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    return out
