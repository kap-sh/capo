"""Generated from Smithy shape ``com.amazonaws.wafregional#GetIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetIPSetRequest(TypedDict, closed=True):
    ip_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to get. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIPSetRequest) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIPSetRequest:
    out: GetIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("IPSetId") is not None:
        out["ip_set_id"] = data["IPSetId"]
    else:
        out["ip_set_id"] = ""
    return out
