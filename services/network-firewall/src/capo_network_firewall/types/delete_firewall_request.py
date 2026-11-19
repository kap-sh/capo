"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DeleteFirewallRequest(TypedDict, closed=True):
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    delete_associated_nat_gateways: NotRequired[
        "capo_network_firewall.types.boolean.Boolean"
    ]
    """<p>Specifies whether to delete the NAT gateways that Network Firewall created for a proxy mode firewall when you delete the firewall. You can choose from the following values:</p> <ul> <li> <p> <code>FALSE</code> - Network Firewall detaches the NAT gateways from the firewall and keeps them. This is the default.</p> </li> <li> <p> <code>TRUE</code> - Network Firewall also deletes the NAT gateways. The firewall status stays <code>DELETING</code> until they're deleted. You need permission to call the Amazon EC2 <code>DeleteNatGateway</code> action.</p> </li> </ul> <p>You can't specify <code>TRUE</code> for a firewall that isn't a proxy mode firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallRequest) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "delete_associated_nat_gateways" in value:
        out["DeleteAssociatedNatGateways"] = value["delete_associated_nat_gateways"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallRequest:
    out: DeleteFirewallRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("DeleteAssociatedNatGateways") is not None:
        out["delete_associated_nat_gateways"] = data["DeleteAssociatedNatGateways"]
    return out
