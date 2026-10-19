"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAutomationRuleCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_transcript_points_of_interest
    import capo_connect.types.question_rule_category_automation_condition
    import capo_connect.types.question_rule_category_automation_label


class EvaluationAutomationRuleCategory(TypedDict, closed=True):
    category: "capo_connect.types.question_rule_category_automation_label.QuestionRuleCategoryAutomationLabel"
    """<p>A category label.</p>"""
    condition: "capo_connect.types.question_rule_category_automation_condition.QuestionRuleCategoryAutomationCondition"
    """<p>An automation condition for a Contact Lens category.</p>"""
    points_of_interest: NotRequired[
        "capo_connect.types.evaluation_transcript_points_of_interest.EvaluationTranscriptPointsOfInterest"
    ]
    """<p>A point of interest in a contact transcript that indicates match of condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAutomationRuleCategory) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    import capo_connect.types.question_rule_category_automation_condition

    out["Condition"] = (
        capo_connect.types.question_rule_category_automation_condition.serialize_json(
            value["condition"]
        )
    )
    if "points_of_interest" in value:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["PointsOfInterest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationAutomationRuleCategory:
    out: EvaluationAutomationRuleCategory = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    if data.get("Condition") is not None:
        import capo_connect.types.question_rule_category_automation_condition

        out["condition"] = (
            capo_connect.types.question_rule_category_automation_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_connect.types.question_rule_category_automation_condition.QuestionRuleCategoryAutomationCondition",
            "",
        )
    if data.get("PointsOfInterest") is not None:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["points_of_interest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
