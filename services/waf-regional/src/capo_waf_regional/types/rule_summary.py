"""Generated from Smithy shape ``com.amazonaws.wafregional#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class RuleSummary(TypedDict, closed=True):
    rule_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>Rule</code>. You use <code>RuleId</code> to get more information about a <code>Rule</code> (see <a>GetRule</a>), update a <code>Rule</code> (see <a>UpdateRule</a>), insert a <code>Rule</code> into a <code>WebACL</code> or delete one from a <code>WebACL</code> (see <a>UpdateWebACL</a>), or delete a <code>Rule</code> from AWS WAF (see <a>DeleteRule</a>).</p> <p> <code>RuleId</code> is returned by <a>CreateRule</a> and by <a>ListRules</a>.</p>"""
    name: "capo_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>Rule</a>. You can't change the name of a <code>Rule</code> after you create it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleSummary) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
