"""Generated from Smithy shape ``com.amazonaws.waf#GetWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id


class GetWebACLRequest(TypedDict, closed=True):
    web_acl_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to get. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLRequest:
    out: GetWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLId") is not None:
        out["web_acl_id"] = data["WebACLId"]
    else:
        out["web_acl_id"] = ""
    return out
