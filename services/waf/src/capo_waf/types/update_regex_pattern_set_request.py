"""Generated from Smithy shape ``com.amazonaws.waf#UpdateRegexPatternSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.regex_pattern_set_updates
    import capo_waf.types.resource_id


class UpdateRegexPatternSetRequest(TypedDict, closed=True):
    regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to update. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""
    updates: "capo_waf.types.regex_pattern_set_updates.RegexPatternSetUpdates"
    """<p>An array of <code>RegexPatternSetUpdate</code> objects that you want to insert into or delete from a <a>RegexPatternSet</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    import capo_waf.types.regex_pattern_set_updates

    out["Updates"] = capo_waf.types.regex_pattern_set_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegexPatternSetRequest:
    out: UpdateRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("RegexPatternSetId") is not None:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        out["regex_pattern_set_id"] = ""
    if data.get("Updates") is not None:
        import capo_waf.types.regex_pattern_set_updates

        out["updates"] = (
            capo_waf.types.regex_pattern_set_updates.deserialize_aws_json_1_1(
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
