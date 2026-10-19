"""Generated from Smithy shape ``com.amazonaws.waf#XssMatchSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name
    import capo_waf.types.xss_match_tuples


class XssMatchSet(TypedDict, closed=True):
    xss_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for an <code>XssMatchSet</code>. You use <code>XssMatchSetId</code> to get information about an <code>XssMatchSet</code> (see <a>GetXssMatchSet</a>), update an <code>XssMatchSet</code> (see <a>UpdateXssMatchSet</a>), insert an <code>XssMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete an <code>XssMatchSet</code> from AWS WAF (see <a>DeleteXssMatchSet</a>).</p> <p> <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>The name, if any, of the <code>XssMatchSet</code>.</p>"""
    xss_match_tuples: "capo_waf.types.xss_match_tuples.XssMatchTuples"
    """<p>Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XssMatchSet) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf.types.xss_match_tuples

    out["XssMatchTuples"] = capo_waf.types.xss_match_tuples.serialize_aws_json_1_1(
        value["xss_match_tuples"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> XssMatchSet:
    out: XssMatchSet = {}  # type: ignore[typeddict-item]
    if data.get("XssMatchSetId") is not None:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        out["xss_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("XssMatchTuples") is not None:
        import capo_waf.types.xss_match_tuples

        out["xss_match_tuples"] = (
            capo_waf.types.xss_match_tuples.deserialize_aws_json_1_1(
                data["XssMatchTuples"]
            )
        )
    else:
        out["xss_match_tuples"] = []
    return out
