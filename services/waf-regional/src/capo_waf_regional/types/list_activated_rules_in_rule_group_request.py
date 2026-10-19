"""Generated from Smithy shape ``com.amazonaws.wafregional#ListActivatedRulesInRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.next_marker
    import capo_waf_regional.types.pagination_limit
    import capo_waf_regional.types.resource_id


class ListActivatedRulesInRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: NotRequired["capo_waf_regional.types.resource_id.ResourceId"]
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> for which you want to get a list of <a>ActivatedRule</a> objects.</p>"""
    next_marker: NotRequired["capo_waf_regional.types.next_marker.NextMarker"]
    """<p>If you specify a value for <code>Limit</code> and you have more <code>ActivatedRules</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>ActivatedRules</code>. For the second and subsequent <code>ListActivatedRulesInRuleGroup</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>ActivatedRules</code>.</p>"""
    limit: NotRequired["capo_waf_regional.types.pagination_limit.PaginationLimit"]
    """<p>Specifies the number of <code>ActivatedRules</code> that you want AWS WAF to return for this request. If you have more <code>ActivatedRules</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>ActivatedRules</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActivatedRulesInRuleGroupRequest) -> dict:
    out: dict = {}
    if "rule_group_id" in value:
        out["RuleGroupId"] = value["rule_group_id"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActivatedRulesInRuleGroupRequest:
    out: ListActivatedRulesInRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
