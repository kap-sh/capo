"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_multi_select_question_properties
    import capo_connect.types.evaluation_form_numeric_question_properties
    import capo_connect.types.evaluation_form_single_select_question_properties
    import capo_connect.types.evaluation_form_text_question_properties


class _EvaluationFormQuestionTypeProperties_Numeric(TypedDict, closed=True):
    Numeric: "capo_connect.types.evaluation_form_numeric_question_properties.EvaluationFormNumericQuestionProperties"


class _EvaluationFormQuestionTypeProperties_SingleSelect(TypedDict, closed=True):
    SingleSelect: "capo_connect.types.evaluation_form_single_select_question_properties.EvaluationFormSingleSelectQuestionProperties"


class _EvaluationFormQuestionTypeProperties_Text(TypedDict, closed=True):
    Text: "capo_connect.types.evaluation_form_text_question_properties.EvaluationFormTextQuestionProperties"


class _EvaluationFormQuestionTypeProperties_MultiSelect(TypedDict, closed=True):
    MultiSelect: "capo_connect.types.evaluation_form_multi_select_question_properties.EvaluationFormMultiSelectQuestionProperties"


EvaluationFormQuestionTypeProperties: TypeAlias = (
    _EvaluationFormQuestionTypeProperties_Numeric
    | _EvaluationFormQuestionTypeProperties_SingleSelect
    | _EvaluationFormQuestionTypeProperties_Text
    | _EvaluationFormQuestionTypeProperties_MultiSelect
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionTypeProperties) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationFormQuestionTypeProperties: cannot serialize unknown variant {value.name!r}"
        )
    elif "Numeric" in value:
        import capo_connect.types.evaluation_form_numeric_question_properties

        return {
            "Numeric": capo_connect.types.evaluation_form_numeric_question_properties.serialize_json(
                value["Numeric"]
            )
        }
    elif "SingleSelect" in value:
        import capo_connect.types.evaluation_form_single_select_question_properties

        return {
            "SingleSelect": capo_connect.types.evaluation_form_single_select_question_properties.serialize_json(
                value["SingleSelect"]
            )
        }
    elif "Text" in value:
        import capo_connect.types.evaluation_form_text_question_properties

        return {
            "Text": capo_connect.types.evaluation_form_text_question_properties.serialize_json(
                value["Text"]
            )
        }
    elif "MultiSelect" in value:
        import capo_connect.types.evaluation_form_multi_select_question_properties

        return {
            "MultiSelect": capo_connect.types.evaluation_form_multi_select_question_properties.serialize_json(
                value["MultiSelect"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormQuestionTypeProperties: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormQuestionTypeProperties:
    if data.get("Numeric") is not None:
        import capo_connect.types.evaluation_form_numeric_question_properties

        return {
            "Numeric": capo_connect.types.evaluation_form_numeric_question_properties.deserialize_json(
                data["Numeric"]
            )
        }
    elif data.get("SingleSelect") is not None:
        import capo_connect.types.evaluation_form_single_select_question_properties

        return {
            "SingleSelect": capo_connect.types.evaluation_form_single_select_question_properties.deserialize_json(
                data["SingleSelect"]
            )
        }
    elif data.get("Text") is not None:
        import capo_connect.types.evaluation_form_text_question_properties

        return {
            "Text": capo_connect.types.evaluation_form_text_question_properties.deserialize_json(
                data["Text"]
            )
        }
    elif data.get("MultiSelect") is not None:
        import capo_connect.types.evaluation_form_multi_select_question_properties

        return {
            "MultiSelect": capo_connect.types.evaluation_form_multi_select_question_properties.deserialize_json(
                data["MultiSelect"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EvaluationFormQuestionTypeProperties: no recognized variant key"
        )
