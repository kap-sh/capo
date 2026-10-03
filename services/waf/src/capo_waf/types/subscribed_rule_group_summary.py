"""Generated from Smithy shape ``com.amazonaws.waf#SubscribedRuleGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.metric_name
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class SubscribedRuleGroupSummary(TypedDict, closed=True):
    rule_group_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>RuleGroup</code>.</p>"""
    name: "capo_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <code>RuleGroup</code>. You can't change the name of a <code>RuleGroup</code> after you create it.</p>"""
    metric_name: "capo_waf.types.metric_name.MetricName"
    """<p>A friendly name or description for the metrics for this <code>RuleGroup</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>RuleGroup</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedRuleGroupSummary) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    out["Name"] = value["name"]
    out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribedRuleGroupSummary:
    out: SubscribedRuleGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.rule_group_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.name required")
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.metric_name required")
    return out
