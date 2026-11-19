"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeRuleGroupSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_group_type


class DescribeRuleGroupSummaryRequest(TypedDict, closed=True):
    rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>Required. The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    type: NotRequired["capo_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>The type of rule group you want a summary for. This is a required field.</p> <p>Valid value: <code>STATEFUL</code> </p> <p>Note that <code>STATELESS</code> exists but is not currently supported. If you provide <code>STATELESS</code>, an exception is returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRuleGroupSummaryRequest) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRuleGroupSummaryRequest:
    out: DescribeRuleGroupSummaryRequest = {}  # type: ignore[typeddict-item]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRuleGroupSummaryRequest) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "rule_group_arn" in value:
        out["RuleGroupArn"] = value["rule_group_arn"]
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = capo_network_firewall.types.rule_group_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeRuleGroupSummaryRequest:
    out: DescribeRuleGroupSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("RuleGroupArn") is not None:
        out["rule_group_arn"] = data["RuleGroupArn"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = capo_network_firewall.types.rule_group_type.deserialize_cbor(
            data["Type"]
        )
    return out
