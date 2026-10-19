"""Generated from Smithy shape ``com.amazonaws.wafregional#GetXssMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetXssMatchSetRequest(TypedDict, closed=True):
    xss_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>XssMatchSetId</code> of the <a>XssMatchSet</a> that you want to get. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetXssMatchSetRequest) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetXssMatchSetRequest:
    out: GetXssMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("XssMatchSetId") is not None:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        out["xss_match_set_id"] = ""
    return out
