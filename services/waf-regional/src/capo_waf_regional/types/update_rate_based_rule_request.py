"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRateBasedRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.rate_limit
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.rule_updates


class UpdateRateBasedRuleRequest(TypedDict, closed=True):
    rule_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <code>RateBasedRule</code> that you want to update. <code>RuleId</code> is returned by <code>CreateRateBasedRule</code> and by <a>ListRateBasedRules</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "capo_waf_regional.types.rule_updates.RuleUpdates"
    """<p>An array of <code>RuleUpdate</code> objects that you want to insert into or delete from a <a>RateBasedRule</a>. </p>"""
    rate_limit: "capo_waf_regional.types.rate_limit.RateLimit"
    """<p>The maximum number of requests, which have an identical value in the field specified by the <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRateBasedRuleRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf_regional.types.rule_updates

    out["Updates"] = capo_waf_regional.types.rule_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    out["RateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRateBasedRuleRequest:
    out: UpdateRateBasedRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf_regional.types.rule_updates

        out["updates"] = capo_waf_regional.types.rule_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        out["updates"] = []
    if data.get("RateLimit") is not None:
        out["rate_limit"] = data["RateLimit"]
    else:
        out["rate_limit"] = 0
    return out
