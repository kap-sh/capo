"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AcceptNetworkFirewallTransitGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.transit_gateway_attachment_id


class AcceptNetworkFirewallTransitGatewayAttachmentRequest(TypedDict, closed=True):
    transit_gateway_attachment_id: "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    """<p>Required. The unique identifier of the transit gateway attachment to accept. This ID is returned in the response when creating a transit gateway-attached firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: AcceptNetworkFirewallTransitGatewayAttachmentRequest,
) -> dict:
    out: dict = {}
    out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AcceptNetworkFirewallTransitGatewayAttachmentRequest:
    out: AcceptNetworkFirewallTransitGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayAttachmentId") is not None:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    else:
        out["transit_gateway_attachment_id"] = ""
    return out
