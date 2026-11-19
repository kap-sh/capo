"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SyncState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.attachment
    import capo_network_firewall.types.nat_gateway_attachments_list
    import capo_network_firewall.types.sync_state_config


class SyncState(TypedDict, closed=True):
    attachment: NotRequired["capo_network_firewall.types.attachment.Attachment"]
    """<p>The configuration and status for a single firewall subnet. For each configured subnet, Network Firewall creates the attachment by instantiating the firewall endpoint in the subnet so that it's ready to take traffic. </p>"""
    config: NotRequired["capo_network_firewall.types.sync_state_config.SyncStateConfig"]
    """<p>The configuration status of the firewall endpoint in a single VPC subnet. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. </p>"""
    nat_gateway_attachments: NotRequired[
        "capo_network_firewall.types.nat_gateway_attachments_list.NatGatewayAttachmentsList"
    ]
    """<p>The NAT gateway that's attached to a proxy mode firewall in the Availability Zone, and the status of the attachment. To get NAT gateway details, such as IP addresses, use the Amazon EC2 <code>DescribeNatGateways</code> action.</p> <p>A proxy mode firewall is <code>READY</code> when at least one Availability Zone's firewall endpoint and NAT gateway attachment are <code>READY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncState) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_network_firewall.types.attachment

        out["Attachment"] = (
            capo_network_firewall.types.attachment.serialize_aws_json_1_0(
                value["attachment"]
            )
        )
    if "config" in value:
        import capo_network_firewall.types.sync_state_config

        out["Config"] = (
            capo_network_firewall.types.sync_state_config.serialize_aws_json_1_0(
                value["config"]
            )
        )
    if "nat_gateway_attachments" in value:
        import capo_network_firewall.types.nat_gateway_attachments_list

        out["NatGatewayAttachments"] = (
            capo_network_firewall.types.nat_gateway_attachments_list.serialize_aws_json_1_0(
                value["nat_gateway_attachments"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncState:
    out: SyncState = {}  # type: ignore[typeddict-item]
    if data.get("Attachment") is not None:
        import capo_network_firewall.types.attachment

        out["attachment"] = (
            capo_network_firewall.types.attachment.deserialize_aws_json_1_0(
                data["Attachment"]
            )
        )
    if data.get("Config") is not None:
        import capo_network_firewall.types.sync_state_config

        out["config"] = (
            capo_network_firewall.types.sync_state_config.deserialize_aws_json_1_0(
                data["Config"]
            )
        )
    if data.get("NatGatewayAttachments") is not None:
        import capo_network_firewall.types.nat_gateway_attachments_list

        out["nat_gateway_attachments"] = (
            capo_network_firewall.types.nat_gateway_attachments_list.deserialize_aws_json_1_0(
                data["NatGatewayAttachments"]
            )
        )
    return out
