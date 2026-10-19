"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.rule_group_updates


class UpdateRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to update. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""
    updates: "capo_waf_regional.types.rule_group_updates.RuleGroupUpdates"
    """<p>An array of <code>RuleGroupUpdate</code> objects that you want to insert into or delete from a <a>RuleGroup</a>.</p> <p>You can only insert <code>REGULAR</code> rules into a rule group.</p> <p> <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    import capo_waf_regional.types.rule_group_updates

    out["Updates"] = capo_waf_regional.types.rule_group_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleGroupRequest:
    out: UpdateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        out["rule_group_id"] = ""
    if data.get("Updates") is not None:
        import capo_waf_regional.types.rule_group_updates

        out["updates"] = (
            capo_waf_regional.types.rule_group_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        out["updates"] = []
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
