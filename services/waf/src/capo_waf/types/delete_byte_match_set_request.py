"""Generated from Smithy shape ``com.amazonaws.waf#DeleteByteMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteByteMatchSetRequest(TypedDict, closed=True):
    byte_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to delete. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteByteMatchSetRequest) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteByteMatchSetRequest:
    out: DeleteByteMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchSetId") is not None:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        out["byte_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
