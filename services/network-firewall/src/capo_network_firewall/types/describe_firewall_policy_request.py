"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeFirewallPolicyRequest(TypedDict, closed=True):
    firewall_policy_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallPolicyRequest) -> dict:
    out: dict = {}
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallPolicyRequest:
    out: DescribeFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFirewallPolicyRequest) -> dict:
    out: dict = {}
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeFirewallPolicyRequest:
    out: DescribeFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    return out
