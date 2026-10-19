"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteXssMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id


class DeleteXssMatchSetRequest(TypedDict, closed=True):
    xss_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>XssMatchSetId</code> of the <a>XssMatchSet</a> that you want to delete. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteXssMatchSetRequest) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteXssMatchSetRequest:
    out: DeleteXssMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("XssMatchSetId") is not None:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        out["xss_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
