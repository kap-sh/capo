"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class ByteMatchSetSummary(TypedDict, closed=True):
    byte_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> for a <code>ByteMatchSet</code>. You use <code>ByteMatchSetId</code> to get information about a <code>ByteMatchSet</code>, update a <code>ByteMatchSet</code>, remove a <code>ByteMatchSet</code> from a <code>Rule</code>, and delete a <code>ByteMatchSet</code> from AWS WAF.</p> <p> <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""
    name: "capo_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>ByteMatchSet</a>. You can't change <code>Name</code> after you create a <code>ByteMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSetSummary) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ByteMatchSetSummary:
    out: ByteMatchSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchSetId") is not None:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        out["byte_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
