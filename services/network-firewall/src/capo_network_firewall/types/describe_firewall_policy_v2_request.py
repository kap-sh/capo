"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallPolicyV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_output_format


class DescribeFirewallPolicyV2Request(TypedDict, closed=True):
    firewall_policy_v2_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Next Generation policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_v2_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_output_format: NotRequired[
        "capo_network_firewall.types.rule_output_format.RuleOutputFormat"
    ]
    """<p>The format in which to return the rules of any firewall engine rule groups that are embedded in the policy. Specify <code>FIREWALL_RULES</code> for structured <code>FirewallRule</code> objects or <code>RULES_STRING</code> for a Suricata-compatible firewall-mode rule string. If you don't specify a format, Network Firewall returns each embedded rule group in the format you provided it in. Referenced rule groups aren't affected.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallPolicyV2Request) -> dict:
    out: dict = {}
    if "firewall_policy_v2_arn" in value:
        out["FirewallPolicyV2Arn"] = value["firewall_policy_v2_arn"]
    if "firewall_policy_v2_name" in value:
        out["FirewallPolicyV2Name"] = value["firewall_policy_v2_name"]
    if "rule_output_format" in value:
        import capo_network_firewall.types.rule_output_format

        out["RuleOutputFormat"] = (
            capo_network_firewall.types.rule_output_format.serialize_aws_json_1_0(
                value["rule_output_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallPolicyV2Request:
    out: DescribeFirewallPolicyV2Request = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyV2Arn") is not None:
        out["firewall_policy_v2_arn"] = data["FirewallPolicyV2Arn"]
    if data.get("FirewallPolicyV2Name") is not None:
        out["firewall_policy_v2_name"] = data["FirewallPolicyV2Name"]
    if data.get("RuleOutputFormat") is not None:
        import capo_network_firewall.types.rule_output_format

        out["rule_output_format"] = (
            capo_network_firewall.types.rule_output_format.deserialize_aws_json_1_0(
                data["RuleOutputFormat"]
            )
        )
    return out
