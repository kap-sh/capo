"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConditionOperand``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_condition
    import capo_connect.types.evaluation_form_item_enablement_expression


class _EvaluationFormItemEnablementConditionOperand_Expression(TypedDict, closed=True):
    Expression: "capo_connect.types.evaluation_form_item_enablement_expression.EvaluationFormItemEnablementExpression"


class _EvaluationFormItemEnablementConditionOperand_Condition(TypedDict, closed=True):
    Condition: "capo_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"


EvaluationFormItemEnablementConditionOperand: TypeAlias = (
    _EvaluationFormItemEnablementConditionOperand_Expression
    | _EvaluationFormItemEnablementConditionOperand_Condition
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConditionOperand) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationFormItemEnablementConditionOperand: cannot serialize unknown variant {value.name!r}"
        )
    elif "Expression" in value:
        import capo_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": capo_connect.types.evaluation_form_item_enablement_expression.serialize_json(
                value["Expression"]
            )
        }
    elif "Condition" in value:
        import capo_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": capo_connect.types.evaluation_form_item_enablement_condition.serialize_json(
                value["Condition"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormItemEnablementConditionOperand: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormItemEnablementConditionOperand:
    if data.get("Expression") is not None:
        import capo_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": capo_connect.types.evaluation_form_item_enablement_expression.deserialize_json(
                data["Expression"]
            )
        }
    elif data.get("Condition") is not None:
        import capo_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": capo_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EvaluationFormItemEnablementConditionOperand: no recognized variant key"
        )
