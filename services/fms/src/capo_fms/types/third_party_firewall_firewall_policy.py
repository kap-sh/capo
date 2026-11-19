"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallFirewallPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.firewall_policy_id
    import capo_fms.types.firewall_policy_name


class ThirdPartyFirewallFirewallPolicy(TypedDict, closed=True):
    firewall_policy_id: NotRequired[
        "capo_fms.types.firewall_policy_id.FirewallPolicyId"
    ]
    """<p>The ID of the specified firewall policy.</p>"""
    firewall_policy_name: NotRequired[
        "capo_fms.types.firewall_policy_name.FirewallPolicyName"
    ]
    """<p>The name of the specified firewall policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallFirewallPolicy) -> dict:
    out: dict = {}
    if "firewall_policy_id" in value:
        out["FirewallPolicyId"] = value["firewall_policy_id"]
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyFirewallFirewallPolicy:
    out: ThirdPartyFirewallFirewallPolicy = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyId") is not None:
        out["firewall_policy_id"] = data["FirewallPolicyId"]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyFirewallFirewallPolicy) -> dict:
    out: dict = {}
    if "firewall_policy_id" in value:
        out["FirewallPolicyId"] = value["firewall_policy_id"]
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    return out


def deserialize_cbor(data: dict) -> ThirdPartyFirewallFirewallPolicy:
    out: ThirdPartyFirewallFirewallPolicy = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyId") is not None:
        out["firewall_policy_id"] = data["FirewallPolicyId"]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    return out
