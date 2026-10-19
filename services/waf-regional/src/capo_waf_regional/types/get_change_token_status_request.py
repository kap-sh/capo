"""Generated from Smithy shape ``com.amazonaws.wafregional#GetChangeTokenStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token


class GetChangeTokenStatusRequest(TypedDict, closed=True):
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The change token for which you want to get the status. This change token was previously returned in the <code>GetChangeToken</code> response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetChangeTokenStatusRequest) -> dict:
    out: dict = {}
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetChangeTokenStatusRequest:
    out: GetChangeTokenStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    return out
