"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRegexPatternSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetRegexPatternSetRequest(TypedDict, closed=True):
    regex_pattern_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to get. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegexPatternSetRequest:
    out: GetRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexPatternSetId") is not None:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        out["regex_pattern_set_id"] = ""
    return out
