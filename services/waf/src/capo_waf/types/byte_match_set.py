"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.byte_match_tuples
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class ByteMatchSet(TypedDict, closed=True):
    byte_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> for a <code>ByteMatchSet</code>. You use <code>ByteMatchSetId</code> to get information about a <code>ByteMatchSet</code> (see <a>GetByteMatchSet</a>), update a <code>ByteMatchSet</code> (see <a>UpdateByteMatchSet</a>), insert a <code>ByteMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>ByteMatchSet</code> from AWS WAF (see <a>DeleteByteMatchSet</a>).</p> <p> <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>ByteMatchSet</a>. You can't change <code>Name</code> after you create a <code>ByteMatchSet</code>.</p>"""
    byte_match_tuples: "capo_waf.types.byte_match_tuples.ByteMatchTuples"
    """<p>Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchSet) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf.types.byte_match_tuples

    out["ByteMatchTuples"] = capo_waf.types.byte_match_tuples.serialize_aws_json_1_1(
        value["byte_match_tuples"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByteMatchSet:
    out: ByteMatchSet = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchSetId") is not None:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        out["byte_match_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ByteMatchTuples") is not None:
        import capo_waf.types.byte_match_tuples

        out["byte_match_tuples"] = (
            capo_waf.types.byte_match_tuples.deserialize_aws_json_1_1(
                data["ByteMatchTuples"]
            )
        )
    else:
        out["byte_match_tuples"] = []
    return out
