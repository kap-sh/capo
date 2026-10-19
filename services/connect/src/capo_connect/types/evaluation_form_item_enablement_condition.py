"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_condition_operand_list
    import capo_connect.types.evaluation_form_item_enablement_operator


class EvaluationFormItemEnablementCondition(TypedDict, closed=True):
    operands: "capo_connect.types.evaluation_form_item_enablement_condition_operand_list.EvaluationFormItemEnablementConditionOperandList"
    """<p>Operands of the enablement condition.</p>"""
    operator: NotRequired[
        "capo_connect.types.evaluation_form_item_enablement_operator.EvaluationFormItemEnablementOperator"
    ]
    """<p>The operator to be used to be applied to operands if more than one provided. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementCondition) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_condition_operand_list

    out["Operands"] = (
        capo_connect.types.evaluation_form_item_enablement_condition_operand_list.serialize_json(
            value["operands"]
        )
    )
    if "operator" in value:
        import capo_connect.types.evaluation_form_item_enablement_operator

        out["Operator"] = (
            capo_connect.types.evaluation_form_item_enablement_operator.serialize_json(
                value["operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementCondition:
    out: EvaluationFormItemEnablementCondition = {}  # type: ignore[typeddict-item]
    if data.get("Operands") is not None:
        import capo_connect.types.evaluation_form_item_enablement_condition_operand_list

        out["operands"] = (
            capo_connect.types.evaluation_form_item_enablement_condition_operand_list.deserialize_json(
                data["Operands"]
            )
        )
    else:
        out["operands"] = []
    if data.get("Operator") is not None:
        import capo_connect.types.evaluation_form_item_enablement_operator

        out["operator"] = (
            capo_connect.types.evaluation_form_item_enablement_operator.deserialize_json(
                data["Operator"]
            )
        )
    return out
