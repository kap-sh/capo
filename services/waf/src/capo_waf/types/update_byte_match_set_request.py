"""Generated from Smithy shape ``com.amazonaws.waf#UpdateByteMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.byte_match_set_updates
    import capo_waf.types.change_token
    import capo_waf.types.resource_id


class UpdateByteMatchSetRequest(TypedDict, closed=True):
    byte_match_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>ByteMatchSetId</code> of the <a>ByteMatchSet</a> that you want to update. <code>ByteMatchSetId</code> is returned by <a>CreateByteMatchSet</a> and by <a>ListByteMatchSets</a>.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "capo_waf.types.byte_match_set_updates.ByteMatchSetUpdates"
    """<p>An array of <code>ByteMatchSetUpdate</code> objects that you want to insert into or delete from a <a>ByteMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>ByteMatchSetUpdate</a>: Contains <code>Action</code> and <code>ByteMatchTuple</code> </p> </li> <li> <p> <a>ByteMatchTuple</a>: Contains <code>FieldToMatch</code>, <code>PositionalConstraint</code>, <code>TargetString</code>, and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateByteMatchSetRequest) -> dict:
    out: dict = {}
    out["ByteMatchSetId"] = value["byte_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf.types.byte_match_set_updates

    out["Updates"] = capo_waf.types.byte_match_set_updates.serialize_aws_json_1_1(
        value["updates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateByteMatchSetRequest:
    out: UpdateByteMatchSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ByteMatchSetId") is not None:
        out["byte_match_set_id"] = data["ByteMatchSetId"]
    else:
        out["byte_match_set_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf.types.byte_match_set_updates

        out["updates"] = capo_waf.types.byte_match_set_updates.deserialize_aws_json_1_1(
            data["Updates"]
        )
    else:
        out["updates"] = []
    return out
