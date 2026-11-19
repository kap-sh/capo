"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeFirewallRequest(TypedDict, closed=True):
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallRequest) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallRequest:
    out: DescribeFirewallRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFirewallRequest) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeFirewallRequest:
    out: DescribeFirewallRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out
