"""Generated from Smithy shape ``com.amazonaws.waf#UpdateRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id
    import capo_waf.types.rule_updates


class UpdateRuleRequest(TypedDict, closed=True):
    rule_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <code>Rule</code> that you want to update. <code>RuleId</code> is returned by <code>CreateRule</code> and by <a>ListRules</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "capo_waf.types.rule_updates.RuleUpdates"
    """<p>An array of <code>RuleUpdate</code> objects that you want to insert into or delete from a <a>Rule</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>RuleUpdate</a>: Contains <code>Action</code> and <code>Predicate</code> </p> </li> <li> <p> <a>Predicate</a>: Contains <code>DataId</code>, <code>Negated</code>, and <code>Type</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf.types.rule_updates

    out["Updates"] = capo_waf.types.rule_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleRequest:
    out: UpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf.types.rule_updates

        out["updates"] = capo_waf.types.rule_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        out["updates"] = []
    return out
