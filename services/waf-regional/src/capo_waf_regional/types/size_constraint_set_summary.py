"""Generated from Smithy shape ``com.amazonaws.wafregional#SizeConstraintSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class SizeConstraintSetSummary(TypedDict, closed=True):
    size_constraint_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>SizeConstraintSet</code>. You use <code>SizeConstraintSetId</code> to get information about a <code>SizeConstraintSet</code> (see <a>GetSizeConstraintSet</a>), update a <code>SizeConstraintSet</code> (see <a>UpdateSizeConstraintSet</a>), insert a <code>SizeConstraintSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>SizeConstraintSet</code> from AWS WAF (see <a>DeleteSizeConstraintSet</a>).</p> <p> <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>"""
    name: "capo_waf_regional.types.resource_name.ResourceName"
    """<p>The name of the <code>SizeConstraintSet</code>, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetSummary) -> dict:
    out: dict = {}
    out["SizeConstraintSetId"] = value["size_constraint_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SizeConstraintSetSummary:
    out: SizeConstraintSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("SizeConstraintSetId") is not None:
        out["size_constraint_set_id"] = data["SizeConstraintSetId"]
    else:
        out["size_constraint_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
