"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRegexMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetRegexMatchSetRequest(TypedDict, closed=True):
    regex_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to get. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegexMatchSetRequest) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegexMatchSetRequest:
    out: GetRegexMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexMatchSetId") is not None:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        out["regex_match_set_id"] = ""
    return out
