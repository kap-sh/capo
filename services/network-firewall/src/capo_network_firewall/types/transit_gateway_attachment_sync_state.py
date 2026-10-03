"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TransitGatewayAttachmentSyncState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.attachment_id
    import capo_network_firewall.types.transit_gateway_attachment_status
    import capo_network_firewall.types.transit_gateway_attachment_sync_state_message


class TransitGatewayAttachmentSyncState(TypedDict, closed=True):
    attachment_id: NotRequired["capo_network_firewall.types.attachment_id.AttachmentId"]
    """<p>The unique identifier of the transit gateway attachment.</p>"""
    transit_gateway_attachment_status: NotRequired[
        "capo_network_firewall.types.transit_gateway_attachment_status.TransitGatewayAttachmentStatus"
    ]
    """<p>The current status of the transit gateway attachment.</p> <p>Valid values are:</p> <ul> <li> <p> <code>CREATING</code> - The attachment is being created</p> </li> <li> <p> <code>DELETING</code> - The attachment is being deleted</p> </li> <li> <p> <code>DELETED</code> - The attachment has been deleted</p> </li> <li> <p> <code>FAILED</code> - The attachment creation has failed and cannot be recovered</p> </li> <li> <p> <code>ERROR</code> - The attachment is in an error state that might be recoverable</p> </li> <li> <p> <code>READY</code> - The attachment is active and processing traffic</p> </li> <li> <p> <code>PENDING_ACCEPTANCE</code> - The attachment is waiting to be accepted</p> </li> <li> <p> <code>REJECTING</code> - The attachment is in the process of being rejected</p> </li> <li> <p> <code>REJECTED</code> - The attachment has been rejected</p> </li> </ul>"""
    status_message: NotRequired[
        "capo_network_firewall.types.transit_gateway_attachment_sync_state_message.TransitGatewayAttachmentSyncStateMessage"
    ]
    """<p>A message providing additional information about the current status, particularly useful when the transit gateway attachment is in a non-<code>READY</code> state.</p> <p>Valid values are:</p> <ul> <li> <p> <code>CREATING</code> - The attachment is being created</p> </li> <li> <p> <code>DELETING</code> - The attachment is being deleted</p> </li> <li> <p> <code>DELETED</code> - The attachment has been deleted</p> </li> <li> <p> <code>FAILED</code> - The attachment creation has failed and cannot be recovered</p> </li> <li> <p> <code>ERROR</code> - The attachment is in an error state that might be recoverable</p> </li> <li> <p> <code>READY</code> - The attachment is active and processing traffic</p> </li> <li> <p> <code>PENDING_ACCEPTANCE</code> - The attachment is waiting to be accepted</p> </li> <li> <p> <code>REJECTING</code> - The attachment is in the process of being rejected</p> </li> <li> <p> <code>REJECTED</code> - The attachment has been rejected</p> </li> </ul> <p>For information about troubleshooting endpoint failures, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html">Troubleshooting firewall endpoint failures</a> in the <i>Network Firewall Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransitGatewayAttachmentSyncState) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "transit_gateway_attachment_status" in value:
        import capo_network_firewall.types.transit_gateway_attachment_status

        out["TransitGatewayAttachmentStatus"] = (
            capo_network_firewall.types.transit_gateway_attachment_status.serialize_aws_json_1_0(
                value["transit_gateway_attachment_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransitGatewayAttachmentSyncState:
    out: TransitGatewayAttachmentSyncState = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("TransitGatewayAttachmentStatus") is not None:
        import capo_network_firewall.types.transit_gateway_attachment_status

        out["transit_gateway_attachment_status"] = (
            capo_network_firewall.types.transit_gateway_attachment_status.deserialize_aws_json_1_0(
                data["TransitGatewayAttachmentStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
