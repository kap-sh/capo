"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.length_bounded_string
    import capo_fms.types.ordered_remediation_actions


class PossibleRemediationAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>A description of the list of remediation actions.</p>"""
    ordered_remediation_actions: (
        "capo_fms.types.ordered_remediation_actions.OrderedRemediationActions"
    )
    """<p>The ordered list of remediation actions.</p>"""
    is_default_action: "capo_fms.types.boolean.Boolean"
    """<p>Information about whether an action is taken by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_fms.types.ordered_remediation_actions

    out["OrderedRemediationActions"] = (
        capo_fms.types.ordered_remediation_actions.serialize_aws_json_1_1(
            value["ordered_remediation_actions"]
        )
    )
    out["IsDefaultAction"] = value.get("is_default_action", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PossibleRemediationAction:
    out: PossibleRemediationAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("OrderedRemediationActions") is not None:
        import capo_fms.types.ordered_remediation_actions

        out["ordered_remediation_actions"] = (
            capo_fms.types.ordered_remediation_actions.deserialize_aws_json_1_1(
                data["OrderedRemediationActions"]
            )
        )
    else:
        out["ordered_remediation_actions"] = []
    if data.get("IsDefaultAction") is not None:
        out["is_default_action"] = data["IsDefaultAction"]
    else:
        out["is_default_action"] = False
    return out
