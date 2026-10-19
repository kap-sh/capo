"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionAutomationAnswerSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_question_automation_answer_source_type


class EvaluationFormQuestionAutomationAnswerSource(TypedDict, closed=True):
    source_type: "capo_connect.types.evaluation_form_question_automation_answer_source_type.EvaluationFormQuestionAutomationAnswerSourceType"
    """<p>The automation answer source type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionAutomationAnswerSource) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_question_automation_answer_source_type

    out["SourceType"] = (
        capo_connect.types.evaluation_form_question_automation_answer_source_type.serialize_json(
            value["source_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormQuestionAutomationAnswerSource:
    out: EvaluationFormQuestionAutomationAnswerSource = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_connect.types.evaluation_form_question_automation_answer_source_type

        out["source_type"] = (
            capo_connect.types.evaluation_form_question_automation_answer_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_connect.types.evaluation_form_question_automation_answer_source_type.EvaluationFormQuestionAutomationAnswerSourceType",
            "",
        )
    return out
