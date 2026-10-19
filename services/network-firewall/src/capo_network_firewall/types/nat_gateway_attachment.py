"""Generated from Smithy shape ``com.amazonaws.networkfirewall#NatGatewayAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.dns_name
    import capo_network_firewall.types.nat_gateway_attachment_status
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.status_reason


class NatGatewayAttachment(TypedDict, closed=True):
    nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>A unique identifier for the NAT gateway to use with proxy resources.</p>"""
    status: "capo_network_firewall.types.nat_gateway_attachment_status.NatGatewayAttachmentStatus"
    """<p>The current status of the NAT gateway attachment. </p> <p>When this value is <code>READY</code>, the attachment is available to proxy traffic. Otherwise, this value reflects its state, for example <code>CREATING</code> or <code>DELETING</code>.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.status_reason.StatusReason"
    ]
    """<p>If Network Firewall encounters an issue with the NAT gateway attachment, it populates this with an explanation of the problem. </p>"""
    dns_name: NotRequired["capo_network_firewall.types.dns_name.DnsName"]
    """<p>The DNS name that resolves to the firewall's proxy for traffic sent through this NAT gateway attachment. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NatGatewayAttachment) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    import capo_network_firewall.types.nat_gateway_attachment_status

    out["Status"] = (
        capo_network_firewall.types.nat_gateway_attachment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "dns_name" in value:
        out["DnsName"] = value["dns_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NatGatewayAttachment:
    out: NatGatewayAttachment = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        out["nat_gateway_id"] = ""
    if data.get("Status") is not None:
        import capo_network_firewall.types.nat_gateway_attachment_status

        out["status"] = (
            capo_network_firewall.types.nat_gateway_attachment_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_network_firewall.types.nat_gateway_attachment_status.NatGatewayAttachmentStatus",
            "",
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    return out
