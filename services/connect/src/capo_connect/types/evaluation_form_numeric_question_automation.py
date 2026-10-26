"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionAutomation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_question_automation_answer_source
    import capo_connect.types.numeric_question_property_value_automation


class _EvaluationFormNumericQuestionAutomation_PropertyValue(TypedDict, closed=True):
    PropertyValue: "capo_connect.types.numeric_question_property_value_automation.NumericQuestionPropertyValueAutomation"


class _EvaluationFormNumericQuestionAutomation_AnswerSource(TypedDict, closed=True):
    AnswerSource: "capo_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"


EvaluationFormNumericQuestionAutomation: TypeAlias = (
    _EvaluationFormNumericQuestionAutomation_PropertyValue
    | _EvaluationFormNumericQuestionAutomation_AnswerSource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionAutomation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationFormNumericQuestionAutomation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PropertyValue" in value:
        import capo_connect.types.numeric_question_property_value_automation

        return {
            "PropertyValue": capo_connect.types.numeric_question_property_value_automation.serialize_json(
                value["PropertyValue"]
            )
        }
    elif "AnswerSource" in value:
        import capo_connect.types.evaluation_form_question_automation_answer_source

        return {
            "AnswerSource": capo_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["AnswerSource"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormNumericQuestionAutomation: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormNumericQuestionAutomation:
    if data.get("PropertyValue") is not None:
        import capo_connect.types.numeric_question_property_value_automation

        return {
            "PropertyValue": capo_connect.types.numeric_question_property_value_automation.deserialize_json(
                data["PropertyValue"]
            )
        }
    elif data.get("AnswerSource") is not None:
        import capo_connect.types.evaluation_form_question_automation_answer_source

        return {
            "AnswerSource": capo_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EvaluationFormNumericQuestionAutomation: no recognized variant key"
        )
