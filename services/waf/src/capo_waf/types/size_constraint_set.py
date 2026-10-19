"""Generated from Smithy shape ``com.amazonaws.waf#SizeConstraintSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name
    import capo_waf.types.size_constraints


class SizeConstraintSet(TypedDict, closed=True):
    size_constraint_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>SizeConstraintSet</code>. You use <code>SizeConstraintSetId</code> to get information about a <code>SizeConstraintSet</code> (see <a>GetSizeConstraintSet</a>), update a <code>SizeConstraintSet</code> (see <a>UpdateSizeConstraintSet</a>), insert a <code>SizeConstraintSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>SizeConstraintSet</code> from AWS WAF (see <a>DeleteSizeConstraintSet</a>).</p> <p> <code>SizeConstraintSetId</code> is returned by <a>CreateSizeConstraintSet</a> and by <a>ListSizeConstraintSets</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>The name, if any, of the <code>SizeConstraintSet</code>.</p>"""
    size_constraints: "capo_waf.types.size_constraints.SizeConstraints"
    """<p>Specifies the parts of web requests that you want to inspect the size of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSet) -> dict:
    out: dict = {}
    out["SizeConstraintSetId"] = value["size_constraint_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf.types.size_constraints

    out["SizeConstraints"] = capo_waf.types.size_constraints.serialize_aws_json_1_1(
        value["size_constraints"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SizeConstraintSet:
    out: SizeConstraintSet = {}  # type: ignore[typeddict-item]
    if data.get("SizeConstraintSetId") is not None:
        out["size_constraint_set_id"] = data["SizeConstraintSetId"]
    else:
        out["size_constraint_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SizeConstraints") is not None:
        import capo_waf.types.size_constraints

        out["size_constraints"] = (
            capo_waf.types.size_constraints.deserialize_aws_json_1_1(
                data["SizeConstraints"]
            )
        )
    else:
        out["size_constraints"] = []
    return out
