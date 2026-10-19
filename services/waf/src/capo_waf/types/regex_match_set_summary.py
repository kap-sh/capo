"""Generated from Smithy shape ``com.amazonaws.waf#RegexMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class RegexMatchSetSummary(TypedDict, closed=True):
    regex_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> for a <code>RegexMatchSet</code>. You use <code>RegexMatchSetId</code> to get information about a <code>RegexMatchSet</code>, update a <code>RegexMatchSet</code>, remove a <code>RegexMatchSet</code> from a <code>Rule</code>, and delete a <code>RegexMatchSet</code> from AWS WAF.</p> <p> <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    name: "capo_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>RegexMatchSet</a>. You can't change <code>Name</code> after you create a <code>RegexMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSetSummary) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchSetSummary:
    out: RegexMatchSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("RegexMatchSetId") is not None:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        out["regex_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
