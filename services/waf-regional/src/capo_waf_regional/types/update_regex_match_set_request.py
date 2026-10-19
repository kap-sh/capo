"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRegexMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.regex_match_set_updates
    import capo_waf_regional.types.resource_id


class UpdateRegexMatchSetRequest(TypedDict, closed=True):
    regex_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to update. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    updates: "capo_waf_regional.types.regex_match_set_updates.RegexMatchSetUpdates"
    """<p>An array of <code>RegexMatchSetUpdate</code> objects that you want to insert into or delete from a <a>RegexMatchSet</a>. For more information, see <a>RegexMatchTuple</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegexMatchSetRequest) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    import capo_waf_regional.types.regex_match_set_updates

    out["Updates"] = (
        capo_waf_regional.types.regex_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegexMatchSetRequest:
    out: UpdateRegexMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexMatchSetId") is not None:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        out["regex_match_set_id"] = ""
    if data.get("Updates") is not None:
        import capo_waf_regional.types.regex_match_set_updates

        out["updates"] = (
            capo_waf_regional.types.regex_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        out["updates"] = []
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
