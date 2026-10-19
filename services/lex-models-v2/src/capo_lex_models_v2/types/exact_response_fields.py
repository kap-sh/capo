"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExactResponseFields``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.answer_field
    import capo_lex_models_v2.types.question_field


class ExactResponseFields(TypedDict, closed=True):
    question_field: "capo_lex_models_v2.types.question_field.QuestionField"
    """<p>The name of the field that contains the query made to the OpenSearch Service database.</p>"""
    answer_field: "capo_lex_models_v2.types.answer_field.AnswerField"
    """<p>The name of the field that contains the answer to the query made to the OpenSearch Service database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExactResponseFields) -> dict:
    out: dict = {}
    out["questionField"] = value["question_field"]
    out["answerField"] = value["answer_field"]
    return out


def deserialize_json(data: dict) -> ExactResponseFields:
    out: ExactResponseFields = {}  # type: ignore[typeddict-item]
    if data.get("questionField") is not None:
        out["question_field"] = data["questionField"]
    else:
        out["question_field"] = ""
    if data.get("answerField") is not None:
        out["answer_field"] = data["answerField"]
    else:
        out["answer_field"] = ""
    return out
