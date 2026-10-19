"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PutAgentRecommendationFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.feedback_category
    import capo_wellarchitected.types.recommendation_feedback_type


class PutAgentRecommendationFeedbackRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation to provide feedback for.</p>"""
    type: "capo_wellarchitected.types.recommendation_feedback_type.RecommendationFeedbackType"
    """<p>The type of feedback being provided.</p>"""
    feedback_category: NotRequired[
        "capo_wellarchitected.types.feedback_category.FeedbackCategory"
    ]
    """<p>Optional category classifying the nature of the feedback.</p>"""
    comments: NotRequired["str"]
    """<p>Optional comments providing additional context about the feedback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAgentRecommendationFeedbackRequest) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.recommendation_feedback_type

    out["type"] = (
        capo_wellarchitected.types.recommendation_feedback_type.serialize_json(
            value["type"]
        )
    )
    if "feedback_category" in value:
        import capo_wellarchitected.types.feedback_category

        out["feedbackCategory"] = (
            capo_wellarchitected.types.feedback_category.serialize_json(
                value["feedback_category"]
            )
        )
    if "comments" in value:
        out["comments"] = value["comments"]
    return out


def deserialize_json(data: dict) -> PutAgentRecommendationFeedbackRequest:
    out: PutAgentRecommendationFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_wellarchitected.types.recommendation_feedback_type

        out["type"] = (
            capo_wellarchitected.types.recommendation_feedback_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_wellarchitected.types.recommendation_feedback_type.RecommendationFeedbackType",
            "",
        )
    if data.get("feedbackCategory") is not None:
        import capo_wellarchitected.types.feedback_category

        out["feedback_category"] = (
            capo_wellarchitected.types.feedback_category.deserialize_json(
                data["feedbackCategory"]
            )
        )
    if data.get("comments") is not None:
        out["comments"] = data["comments"]
    return out
