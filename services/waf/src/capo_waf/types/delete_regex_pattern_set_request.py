"""Generated from Smithy shape ``com.amazonaws.waf#DeleteRegexPatternSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteRegexPatternSetRequest(TypedDict, closed=True):
    regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to delete. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegexPatternSetRequest:
    out: DeleteRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexPatternSetId") is not None:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        out["regex_pattern_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
