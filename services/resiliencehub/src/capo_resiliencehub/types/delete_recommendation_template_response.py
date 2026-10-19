"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteRecommendationTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.recommendation_template_status


class DeleteRecommendationTemplateResponse(TypedDict, closed=True):
    recommendation_template_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a recommendation template.</p>"""
    status: "capo_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus"
    """<p>Status of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationTemplateResponse) -> dict:
    out: dict = {}
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    import capo_resiliencehub.types.recommendation_template_status

    out["status"] = (
        capo_resiliencehub.types.recommendation_template_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteRecommendationTemplateResponse:
    out: DeleteRecommendationTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationTemplateArn") is not None:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        out["recommendation_template_arn"] = ""
    if data.get("status") is not None:
        import capo_resiliencehub.types.recommendation_template_status

        out["status"] = (
            capo_resiliencehub.types.recommendation_template_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus",
            "",
        )
    return out
