"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallPolicyV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DeleteFirewallPolicyV2Request(TypedDict, closed=True):
    firewall_policy_v2_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Next Generation policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_v2_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallPolicyV2Request) -> dict:
    out: dict = {}
    if "firewall_policy_v2_arn" in value:
        out["FirewallPolicyV2Arn"] = value["firewall_policy_v2_arn"]
    if "firewall_policy_v2_name" in value:
        out["FirewallPolicyV2Name"] = value["firewall_policy_v2_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallPolicyV2Request:
    out: DeleteFirewallPolicyV2Request = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyV2Arn") is not None:
        out["firewall_policy_v2_arn"] = data["FirewallPolicyV2Arn"]
    if data.get("FirewallPolicyV2Name") is not None:
        out["firewall_policy_v2_name"] = data["FirewallPolicyV2Name"]
    return out
