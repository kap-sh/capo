"""Generated from Smithy shape ``com.amazonaws.waf#DeleteIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class DeleteIPSetRequest(TypedDict, closed=True):
    ip_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to delete. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIPSetRequest) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIPSetRequest:
    out: DeleteIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IPSetId") is not None:
        out["ip_set_id"] = data["IPSetId"]
    else:
        out["ip_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
