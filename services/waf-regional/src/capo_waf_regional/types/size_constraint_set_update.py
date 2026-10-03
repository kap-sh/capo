"""Generated from Smithy shape ``com.amazonaws.wafregional#SizeConstraintSetUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.change_action
    import capo_waf_regional.types.size_constraint


class SizeConstraintSetUpdate(TypedDict, closed=True):
    action: "capo_waf_regional.types.change_action.ChangeAction"
    """<p>Specify <code>INSERT</code> to add a <a>SizeConstraintSetUpdate</a> to a <a>SizeConstraintSet</a>. Use <code>DELETE</code> to remove a <code>SizeConstraintSetUpdate</code> from a <code>SizeConstraintSet</code>.</p>"""
    size_constraint: "capo_waf_regional.types.size_constraint.SizeConstraint"
    """<p>Specifies a constraint on the size of a part of the web request. AWS WAF uses the <code>Size</code>, <code>ComparisonOperator</code>, and <code>FieldToMatch</code> to build an expression in the form of "<code>Size</code> <code>ComparisonOperator</code> size in bytes of <code>FieldToMatch</code>". If that expression is true, the <code>SizeConstraint</code> is considered to match.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintSetUpdate) -> dict:
    out: dict = {}
    import capo_waf_regional.types.change_action

    out["Action"] = capo_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import capo_waf_regional.types.size_constraint

    out["SizeConstraint"] = (
        capo_waf_regional.types.size_constraint.serialize_aws_json_1_1(
            value["size_constraint"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SizeConstraintSetUpdate:
    out: SizeConstraintSetUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf_regional.types.change_action

        out["action"] = capo_waf_regional.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("SizeConstraintSetUpdate.action required")
    if data.get("SizeConstraint") is not None:
        import capo_waf_regional.types.size_constraint

        out["size_constraint"] = (
            capo_waf_regional.types.size_constraint.deserialize_aws_json_1_1(
                data["SizeConstraint"]
            )
        )
    else:
        raise DeserializationError("SizeConstraintSetUpdate.size_constraint required")
    return out
