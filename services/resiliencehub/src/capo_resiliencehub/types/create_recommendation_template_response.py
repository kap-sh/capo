"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateRecommendationTemplateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.recommendation_template


class CreateRecommendationTemplateResponse(TypedDict, closed=True):
    recommendation_template: NotRequired[
        "capo_resiliencehub.types.recommendation_template.RecommendationTemplate"
    ]
    """<p>The newly created recommendation template, returned as an object. This object includes the template's name, format, status, tags, Amazon S3 bucket location, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommendationTemplateResponse) -> dict:
    out: dict = {}
    if "recommendation_template" in value:
        import capo_resiliencehub.types.recommendation_template

        out["recommendationTemplate"] = (
            capo_resiliencehub.types.recommendation_template.serialize_json(
                value["recommendation_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecommendationTemplateResponse:
    out: CreateRecommendationTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationTemplate") is not None:
        import capo_resiliencehub.types.recommendation_template

        out["recommendation_template"] = (
            capo_resiliencehub.types.recommendation_template.deserialize_json(
                data["recommendationTemplate"]
            )
        )
    return out


def redact_sensitive(value: CreateRecommendationTemplateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation_template" in value:
        import capo_resiliencehub.types.recommendation_template

        out["recommendation_template"] = (
            capo_resiliencehub.types.recommendation_template.redact_sensitive(
                value["recommendation_template"]
            )
        )
    return out
