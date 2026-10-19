"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteRecommendationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token


class DeleteRecommendationTemplateRequest(TypedDict, closed=True):
    recommendation_template_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a recommendation template.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationTemplateRequest) -> dict:
    out: dict = {}
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteRecommendationTemplateRequest:
    out: DeleteRecommendationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommendationTemplateArn") is not None:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        out["recommendation_template_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
