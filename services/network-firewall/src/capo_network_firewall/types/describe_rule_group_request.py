"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.rule_output_format


class DescribeRuleGroupRequest(TypedDict, closed=True):
    rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    type: NotRequired["capo_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates the type of the rule group. Valid values are:</p> <ul> <li> <p> <code>STATELESS</code> - Stateless rules, for use in a Classic Network Firewall policy.</p> </li> <li> <p> <code>STATEFUL</code> - Stateful rules, for use in a Classic Network Firewall policy.</p> </li> <li> <p> <code>FIREWALL</code> - Firewall engine rules, for use in a Next Generation policy.</p> </li> <li> <p> <code>IPS</code> - IPS engine rules, for use in a Next Generation policy.</p> </li> </ul> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>"""
    analyze_rule_group: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis.</p>"""
    rule_output_format: NotRequired[
        "capo_network_firewall.types.rule_output_format.RuleOutputFormat"
    ]
    """<p>For a firewall engine rule group, the format in which to return the rules. Specify one of the following values:</p> <ul> <li> <p> <code>FIREWALL_RULES</code> - Returns the rules as structured <code>FirewallRule</code> objects.</p> </li> <li> <p> <code>RULES_STRING</code> - Returns the rules as a Suricata-compatible firewall-mode rule string.</p> </li> </ul> <p>If you don't specify a format, Network Firewall returns the rules in the format you provided them in. This setting applies only to <code>FIREWALL</code> and <code>IPS</code> rule groups; IPS engine rule groups support only <code>RULES_STRING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupRequest) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "rule_group_arn" in value:
        out["RuleGroupArn"] = value["rule_group_arn"]
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = (
            capo_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "analyze_rule_group" in value:
        out["AnalyzeRuleGroup"] = value["analyze_rule_group"]
    if "rule_output_format" in value:
        import capo_network_firewall.types.rule_output_format

        out["RuleOutputFormat"] = (
            capo_network_firewall.types.rule_output_format.serialize_aws_json_1_0(
                value["rule_output_format"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupRequest:
    out: DescribeRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("RuleGroupArn") is not None:
        out["rule_group_arn"] = data["RuleGroupArn"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = (
            capo_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if data.get("AnalyzeRuleGroup") is not None:
        out["analyze_rule_group"] = data["AnalyzeRuleGroup"]
    if data.get("RuleOutputFormat") is not None:
        import capo_network_firewall.types.rule_output_format

        out["rule_output_format"] = (
            capo_network_firewall.types.rule_output_format.deserialize_aws_json_1_0(
                data["RuleOutputFormat"]
            )
        )
    return out
