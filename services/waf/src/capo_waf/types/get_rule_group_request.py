"""Generated from Smithy shape ``com.amazonaws.waf#GetRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id


class GetRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to get. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleGroupRequest:
    out: GetRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        out["rule_group_id"] = ""
    return out
