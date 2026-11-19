"""Generated from Smithy shape ``com.amazonaws.connect#SingleSelectQuestionAutomationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_condition
    import capo_connect.types.reference_id


class SingleSelectQuestionAutomationRule(TypedDict, closed=True):
    condition: "capo_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"
    """<p>The condition that must be satisfied for the answer option to be selected. The condition uses the same sources, comparators, and operators as item enablement conditions.</p>"""
    option_ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the answer option to select when the condition is satisfied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleSelectQuestionAutomationRule) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_condition

    out["Condition"] = (
        capo_connect.types.evaluation_form_item_enablement_condition.serialize_json(
            value["condition"]
        )
    )
    out["OptionRefId"] = value["option_ref_id"]
    return out


def deserialize_json(data: dict) -> SingleSelectQuestionAutomationRule:
    out: SingleSelectQuestionAutomationRule = {}  # type: ignore[typeddict-item]
    if data.get("Condition") is not None:
        import capo_connect.types.evaluation_form_item_enablement_condition

        out["condition"] = (
            capo_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "SingleSelectQuestionAutomationRule.condition required"
        )
    if data.get("OptionRefId") is not None:
        out["option_ref_id"] = data["OptionRefId"]
    else:
        out["option_ref_id"] = ""
    return out
