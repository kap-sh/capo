"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn


class DescribeFirewallMetadataRequest(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallMetadataRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallMetadataRequest:
    out: DescribeFirewallMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFirewallMetadataRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeFirewallMetadataRequest:
    out: DescribeFirewallMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out
