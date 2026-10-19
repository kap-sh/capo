"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.automatic_fail_configuration
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_form_multi_select_question_option_text
    import capo_connect.types.evaluation_form_question_answer_score
    import capo_connect.types.question_option_points_configuration
    import capo_connect.types.reference_id


class EvaluationFormMultiSelectQuestionOption(TypedDict, closed=True):
    ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>Reference identifier for this option.</p>"""
    text: "capo_connect.types.evaluation_form_multi_select_question_option_text.EvaluationFormMultiSelectQuestionOptionText"
    """<p>Display text for this option.</p>"""
    score: "capo_connect.types.evaluation_form_question_answer_score.EvaluationFormQuestionAnswerScore"
    """<p>The score assigned to the answer option.</p>"""
    automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.</p>"""
    automatic_fail_configuration: NotRequired[
        "capo_connect.types.automatic_fail_configuration.AutomaticFailConfiguration"
    ]
    points_configuration: NotRequired[
        "capo_connect.types.question_option_points_configuration.QuestionOptionPointsConfiguration"
    ]
    """<p>The points configuration for point-based scoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionOption) -> dict:
    out: dict = {}
    out["RefId"] = value["ref_id"]
    out["Text"] = value["text"]
    out["Score"] = value.get("score", 0)
    out["AutomaticFail"] = value.get("automatic_fail", False)
    if "automatic_fail_configuration" in value:
        import capo_connect.types.automatic_fail_configuration

        out["AutomaticFailConfiguration"] = (
            capo_connect.types.automatic_fail_configuration.serialize_json(
                value["automatic_fail_configuration"]
            )
        )
    if "points_configuration" in value:
        import capo_connect.types.question_option_points_configuration

        out["PointsConfiguration"] = (
            capo_connect.types.question_option_points_configuration.serialize_json(
                value["points_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionOption:
    out: EvaluationFormMultiSelectQuestionOption = {}  # type: ignore[typeddict-item]
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    else:
        out["ref_id"] = ""
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("Score") is not None:
        out["score"] = data["Score"]
    else:
        out["score"] = 0
    if data.get("AutomaticFail") is not None:
        out["automatic_fail"] = data["AutomaticFail"]
    else:
        out["automatic_fail"] = False
    if data.get("AutomaticFailConfiguration") is not None:
        import capo_connect.types.automatic_fail_configuration

        out["automatic_fail_configuration"] = (
            capo_connect.types.automatic_fail_configuration.deserialize_json(
                data["AutomaticFailConfiguration"]
            )
        )
    if data.get("PointsConfiguration") is not None:
        import capo_connect.types.question_option_points_configuration

        out["points_configuration"] = (
            capo_connect.types.question_option_points_configuration.deserialize_json(
                data["PointsConfiguration"]
            )
        )
    return out
