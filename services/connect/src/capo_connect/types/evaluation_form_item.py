"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_question
    import capo_connect.types.evaluation_form_section


class _EvaluationFormItem_Section(TypedDict, closed=True):
    Section: "capo_connect.types.evaluation_form_section.EvaluationFormSection"


class _EvaluationFormItem_Question(TypedDict, closed=True):
    Question: "capo_connect.types.evaluation_form_question.EvaluationFormQuestion"


EvaluationFormItem: TypeAlias = (
    _EvaluationFormItem_Section | _EvaluationFormItem_Question | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItem) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationFormItem: cannot serialize unknown variant {value.name!r}"
        )
    elif "Section" in value:
        import capo_connect.types.evaluation_form_section

        return {
            "Section": capo_connect.types.evaluation_form_section.serialize_json(
                value["Section"]
            )
        }
    elif "Question" in value:
        import capo_connect.types.evaluation_form_question

        return {
            "Question": capo_connect.types.evaluation_form_question.serialize_json(
                value["Question"]
            )
        }
    else:
        raise SerializationError("EvaluationFormItem: no variant present")


def deserialize_json(data: dict) -> EvaluationFormItem:
    if data.get("Section") is not None:
        import capo_connect.types.evaluation_form_section

        return {
            "Section": capo_connect.types.evaluation_form_section.deserialize_json(
                data["Section"]
            )
        }
    elif data.get("Question") is not None:
        import capo_connect.types.evaluation_form_question

        return {
            "Question": capo_connect.types.evaluation_form_question.deserialize_json(
                data["Question"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluationFormItem: no recognized variant key")
