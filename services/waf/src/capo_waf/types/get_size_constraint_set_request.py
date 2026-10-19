"""Generated from Smithy shape ``com.amazonaws.waf#GetSizeConstraintSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id


class GetSizeConstraintSetRequest(TypedDict, closed=True):
    size_constraint_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>SizeConstraintSetId</code> of the <a>SizeConstraintSet</a> that you want to get. <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSizeConstraintSetRequest) -> dict:
    out: dict = {}
    out["SizeConstraintSetId"] = value["size_constraint_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSizeConstraintSetRequest:
    out: GetSizeConstraintSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("SizeConstraintSetId") is not None:
        out["size_constraint_set_id"] = data["SizeConstraintSetId"]
    else:
        out["size_constraint_set_id"] = ""
    return out
