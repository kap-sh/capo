"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.transit_gateway_connect_peer_arn


class AssociateTransitGatewayConnectPeerRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_connect_peer_arn: "capo_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn"
    """<p>The Amazon Resource Name (ARN) of the Connect peer.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTransitGatewayConnectPeerRequest) -> dict:
    out: dict = {}
    out["TransitGatewayConnectPeerArn"] = value["transit_gateway_connect_peer_arn"]
    out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateTransitGatewayConnectPeerRequest:
    out: AssociateTransitGatewayConnectPeerRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayConnectPeerArn") is not None:
        out["transit_gateway_connect_peer_arn"] = data["TransitGatewayConnectPeerArn"]
    else:
        out["transit_gateway_connect_peer_arn"] = ""
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    return out
