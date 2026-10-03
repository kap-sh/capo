"""Generated from Smithy shape ``com.amazonaws.wafv2#DescribeManagedRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.capacity_unit
    import capo_wafv2.types.label_name
    import capo_wafv2.types.label_summaries
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.rule_summaries
    import capo_wafv2.types.version_key_string


class DescribeManagedRuleGroupResponse(TypedDict, closed=True):
    version_name: NotRequired["capo_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The managed rule group's version. </p>"""
    sns_topic_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic that's used to provide notification of changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/welcome.html">Amazon Simple Notification Service Developer Guide</a>.</p>"""
    capacity: NotRequired["capo_wafv2.types.capacity_unit.CapacityUnit"]
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    rules: NotRequired["capo_wafv2.types.rule_summaries.RuleSummaries"]
    """<p></p>"""
    label_namespace: NotRequired["capo_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for a managed rule group is the following: </p> <p> <code>awswaf:managed:<vendor>:<rule group name></code>:</p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""
    available_labels: NotRequired["capo_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the <code>RuleLabels</code> for a <a>Rule</a>.</p>"""
    consumed_labels: NotRequired["capo_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a <code>LabelMatchStatement</code> specification, in the <a>Statement</a> definition of a rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedRuleGroupResponse) -> dict:
    out: dict = {}
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "rules" in value:
        import capo_wafv2.types.rule_summaries

        out["Rules"] = capo_wafv2.types.rule_summaries.serialize_aws_json_1_1(
            value["rules"]
        )
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    if "available_labels" in value:
        import capo_wafv2.types.label_summaries

        out["AvailableLabels"] = (
            capo_wafv2.types.label_summaries.serialize_aws_json_1_1(
                value["available_labels"]
            )
        )
    if "consumed_labels" in value:
        import capo_wafv2.types.label_summaries

        out["ConsumedLabels"] = capo_wafv2.types.label_summaries.serialize_aws_json_1_1(
            value["consumed_labels"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedRuleGroupResponse:
    out: DescribeManagedRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    if data.get("Rules") is not None:
        import capo_wafv2.types.rule_summaries

        out["rules"] = capo_wafv2.types.rule_summaries.deserialize_aws_json_1_1(
            data["Rules"]
        )
    if data.get("LabelNamespace") is not None:
        out["label_namespace"] = data["LabelNamespace"]
    if data.get("AvailableLabels") is not None:
        import capo_wafv2.types.label_summaries

        out["available_labels"] = (
            capo_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["AvailableLabels"]
            )
        )
    if data.get("ConsumedLabels") is not None:
        import capo_wafv2.types.label_summaries

        out["consumed_labels"] = (
            capo_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["ConsumedLabels"]
            )
        )
    return out
