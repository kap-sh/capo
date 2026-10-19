"""Generated from Smithy shape ``com.amazonaws.waf#GetRateBasedRuleManagedKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.next_marker
    import capo_waf.types.resource_id


class GetRateBasedRuleManagedKeysRequest(TypedDict, closed=True):
    rule_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <a>RateBasedRule</a> for which you want to get a list of <code>ManagedKeys</code>. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>"""
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p>A null value and not currently used. Do not include this in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleManagedKeysRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleManagedKeysRequest:
    out: GetRateBasedRuleManagedKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
