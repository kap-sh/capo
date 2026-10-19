"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.policy_string
    import capo_network_firewall.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the account that you want to share your Network Firewall resources with.</p>"""
    policy: "capo_network_firewall.types.policy_string.PolicyString"
    """<p>The IAM policy statement that lists the accounts that you want to share your Network Firewall resources with and the operations that you want the accounts to be able to perform. </p> <p>For a rule group resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:CreateFirewallPolicy</p> </li> <li> <p>network-firewall:UpdateFirewallPolicy</p> </li> <li> <p>network-firewall:ListRuleGroups</p> </li> </ul> <p>For a firewall policy resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:AssociateFirewallPolicy</p> </li> <li> <p>network-firewall:ListFirewallPolicies</p> </li> </ul> <p>For a firewall resource, you can specify the following operations in the Actions section of the statement:</p> <ul> <li> <p>network-firewall:CreateVpcEndpointAssociation</p> </li> <li> <p>network-firewall:DescribeFirewallMetadata</p> </li> <li> <p>network-firewall:ListFirewalls</p> </li> </ul> <p>In the Resource section of the statement, you specify the ARNs for the Network Firewall resources that you want to share with the account that you specified in <code>Arn</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
