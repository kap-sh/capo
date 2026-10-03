"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RejectNetworkFirewallTransitGatewayAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.transit_gateway_attachment_id
    import capo_network_firewall.types.transit_gateway_attachment_status


class RejectNetworkFirewallTransitGatewayAttachmentResponse(TypedDict, closed=True):
    transit_gateway_attachment_id: "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    """<p>The unique identifier of the transit gateway attachment that was rejected.</p>"""
    transit_gateway_attachment_status: "capo_network_firewall.types.transit_gateway_attachment_status.TransitGatewayAttachmentStatus"
    """<p>The current status of the transit gateway attachment. Valid values are:</p> <ul> <li> <p> <code>CREATING</code> - The attachment is being created</p> </li> <li> <p> <code>DELETING</code> - The attachment is being deleted</p> </li> <li> <p> <code>DELETED</code> - The attachment has been deleted</p> </li> <li> <p> <code>FAILED</code> - The attachment creation has failed and cannot be recovered</p> </li> <li> <p> <code>ERROR</code> - The attachment is in an error state that might be recoverable</p> </li> <li> <p> <code>READY</code> - The attachment is active and processing traffic</p> </li> <li> <p> <code>PENDING_ACCEPTANCE</code> - The attachment is waiting to be accepted</p> </li> <li> <p> <code>REJECTING</code> - The attachment is in the process of being rejected</p> </li> <li> <p> <code>REJECTED</code> - The attachment has been rejected</p> </li> </ul> <p>For information about troubleshooting endpoint failures, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html">Troubleshooting firewall endpoint failures</a> in the <i>Network Firewall Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: RejectNetworkFirewallTransitGatewayAttachmentResponse,
) -> dict:
    out: dict = {}
    out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    import capo_network_firewall.types.transit_gateway_attachment_status

    out["TransitGatewayAttachmentStatus"] = (
        capo_network_firewall.types.transit_gateway_attachment_status.serialize_aws_json_1_0(
            value["transit_gateway_attachment_status"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> RejectNetworkFirewallTransitGatewayAttachmentResponse:
    out: RejectNetworkFirewallTransitGatewayAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransitGatewayAttachmentId") is not None:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    else:
        raise DeserializationError(
            "RejectNetworkFirewallTransitGatewayAttachmentResponse.transit_gateway_attachment_id required"
        )
    if data.get("TransitGatewayAttachmentStatus") is not None:
        import capo_network_firewall.types.transit_gateway_attachment_status

        out["transit_gateway_attachment_status"] = (
            capo_network_firewall.types.transit_gateway_attachment_status.deserialize_aws_json_1_0(
                data["TransitGatewayAttachmentStatus"]
            )
        )
    else:
        raise DeserializationError(
            "RejectNetworkFirewallTransitGatewayAttachmentResponse.transit_gateway_attachment_status required"
        )
    return out
