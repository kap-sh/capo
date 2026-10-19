"""Generated from Smithy shape ``com.amazonaws.wafregional#XssMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class XssMatchSetSummary(TypedDict, closed=True):
    xss_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for an <code>XssMatchSet</code>. You use <code>XssMatchSetId</code> to get information about a <code>XssMatchSet</code> (see <a>GetXssMatchSet</a>), update an <code>XssMatchSet</code> (see <a>UpdateXssMatchSet</a>), insert an <code>XssMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete an <code>XssMatchSet</code> from AWS WAF (see <a>DeleteXssMatchSet</a>).</p> <p> <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""
    name: "capo_waf_regional.types.resource_name.ResourceName"
    """<p>The name of the <code>XssMatchSet</code>, if any, specified by <code>Id</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSetSummary) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XssMatchSetSummary:
    out: XssMatchSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("XssMatchSetId") is not None:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        out["xss_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
