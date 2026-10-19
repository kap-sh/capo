"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRateBasedRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetRateBasedRuleRequest(TypedDict, closed=True):
    rule_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <a>RateBasedRule</a> that you want to get. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleRequest:
    out: GetRateBasedRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    return out
