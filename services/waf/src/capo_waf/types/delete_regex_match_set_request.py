"""Generated from Smithy shape ``com.amazonaws.waf#DeleteRegexMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteRegexMatchSetRequest(TypedDict, closed=True):
    regex_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to delete. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegexMatchSetRequest) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegexMatchSetRequest:
    out: DeleteRegexMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexMatchSetId") is not None:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        out["regex_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
