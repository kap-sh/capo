"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_answer_data
    import capo_connect.types.evaluation_question_answer_analysis_details
    import capo_connect.types.evaluation_question_answer_analysis_type
    import capo_connect.types.evaluation_question_input_details
    import capo_connect.types.evaluation_suggested_answer_status


class EvaluationSuggestedAnswer(TypedDict, closed=True):
    value: NotRequired["capo_connect.types.evaluation_answer_data.EvaluationAnswerData"]
    status: "capo_connect.types.evaluation_suggested_answer_status.EvaluationSuggestedAnswerStatus"
    """<p>The status of the suggested answer. D</p>"""
    input: NotRequired[
        "capo_connect.types.evaluation_question_input_details.EvaluationQuestionInputDetails"
    ]
    """<p>Details about the input used to question automation.</p>"""
    analysis_type: "capo_connect.types.evaluation_question_answer_analysis_type.EvaluationQuestionAnswerAnalysisType"
    """<p>Type of analysis used to provide suggested answer.</p>"""
    analysis_details: NotRequired[
        "capo_connect.types.evaluation_question_answer_analysis_details.EvaluationQuestionAnswerAnalysisDetails"
    ]
    """<p>Detailed analysis results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSuggestedAnswer) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_connect.types.evaluation_answer_data

        out["Value"] = capo_connect.types.evaluation_answer_data.serialize_json(
            value["value"]
        )
    import capo_connect.types.evaluation_suggested_answer_status

    out["Status"] = (
        capo_connect.types.evaluation_suggested_answer_status.serialize_json(
            value["status"]
        )
    )
    if "input" in value:
        import capo_connect.types.evaluation_question_input_details

        out["Input"] = (
            capo_connect.types.evaluation_question_input_details.serialize_json(
                value["input"]
            )
        )
    import capo_connect.types.evaluation_question_answer_analysis_type

    out["AnalysisType"] = (
        capo_connect.types.evaluation_question_answer_analysis_type.serialize_json(
            value["analysis_type"]
        )
    )
    if "analysis_details" in value:
        import capo_connect.types.evaluation_question_answer_analysis_details

        out["AnalysisDetails"] = (
            capo_connect.types.evaluation_question_answer_analysis_details.serialize_json(
                value["analysis_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSuggestedAnswer:
    out: EvaluationSuggestedAnswer = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        import capo_connect.types.evaluation_answer_data

        out["value"] = capo_connect.types.evaluation_answer_data.deserialize_json(
            data["Value"]
        )
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_suggested_answer_status

        out["status"] = (
            capo_connect.types.evaluation_suggested_answer_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_suggested_answer_status.EvaluationSuggestedAnswerStatus",
            "",
        )
    if data.get("Input") is not None:
        import capo_connect.types.evaluation_question_input_details

        out["input"] = (
            capo_connect.types.evaluation_question_input_details.deserialize_json(
                data["Input"]
            )
        )
    if data.get("AnalysisType") is not None:
        import capo_connect.types.evaluation_question_answer_analysis_type

        out["analysis_type"] = (
            capo_connect.types.evaluation_question_answer_analysis_type.deserialize_json(
                data["AnalysisType"]
            )
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_connect.types.evaluation_question_answer_analysis_type.EvaluationQuestionAnswerAnalysisType",
            "",
        )
    if data.get("AnalysisDetails") is not None:
        import capo_connect.types.evaluation_question_answer_analysis_details

        out["analysis_details"] = (
            capo_connect.types.evaluation_question_answer_analysis_details.deserialize_json(
                data["AnalysisDetails"]
            )
        )
    return out
