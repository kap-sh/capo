"""Generated from Smithy shape ``com.amazonaws.wafregional#GetByteMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id


class GetByteMatchSetRequest(TypedDict, closed=True):
    byte_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to get. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetByteMatchSetRequest) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetByteMatchSetRequest:
    out: GetByteMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchSetId") is not None:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        out["byte_match_set_id"] = ""
    return out
