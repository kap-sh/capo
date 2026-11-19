"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.transit_gateway_attachment_id


class FirewallMetadata(TypedDict, closed=True):
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "capo_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The unique identifier of the transit gateway attachment associated with this firewall. This field is only present for transit gateway-attached firewalls.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallMetadata) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "transit_gateway_attachment_id" in value:
        out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallMetadata:
    out: FirewallMetadata = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("TransitGatewayAttachmentId") is not None:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallMetadata) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "transit_gateway_attachment_id" in value:
        out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    return out


def deserialize_cbor(data: dict) -> FirewallMetadata:
    out: FirewallMetadata = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("TransitGatewayAttachmentId") is not None:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    return out
