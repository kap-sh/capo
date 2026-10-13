"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListRecommendationTemplatesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.next_token
    import capo_resiliencehub.types.recommendation_template_list


class ListRecommendationTemplatesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    recommendation_templates: NotRequired[
        "capo_resiliencehub.types.recommendation_template_list.RecommendationTemplateList"
    ]
    """<p>The recommendation templates for the Resilience Hub applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationTemplatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_templates" in value:
        import capo_resiliencehub.types.recommendation_template_list

        out["recommendationTemplates"] = (
            capo_resiliencehub.types.recommendation_template_list.serialize_json(
                value["recommendation_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommendationTemplatesResponse:
    out: ListRecommendationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationTemplates") is not None:
        import capo_resiliencehub.types.recommendation_template_list

        out["recommendation_templates"] = (
            capo_resiliencehub.types.recommendation_template_list.deserialize_json(
                data["recommendationTemplates"]
            )
        )
    return out


def redact_sensitive(value: ListRecommendationTemplatesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation_templates" in value:
        import capo_resiliencehub.types.recommendation_template_list

        out["recommendation_templates"] = (
            capo_resiliencehub.types.recommendation_template_list.redact_sensitive(
                value["recommendation_templates"]
            )
        )
    return out
