"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetOrganizationRecommendationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation


class GetOrganizationRecommendationResponse(TypedDict, closed=True):
    organization_recommendation: NotRequired[
        "capo_trustedadvisor.types.organization_recommendation.OrganizationRecommendation"
    ]
    """<p>The Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationRecommendationResponse) -> dict:
    out: dict = {}
    if "organization_recommendation" in value:
        import capo_trustedadvisor.types.organization_recommendation

        out["organizationRecommendation"] = (
            capo_trustedadvisor.types.organization_recommendation.serialize_json(
                value["organization_recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOrganizationRecommendationResponse:
    out: GetOrganizationRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("organizationRecommendation") is not None:
        import capo_trustedadvisor.types.organization_recommendation

        out["organization_recommendation"] = (
            capo_trustedadvisor.types.organization_recommendation.deserialize_json(
                data["organizationRecommendation"]
            )
        )
    return out


def redact_sensitive(value: GetOrganizationRecommendationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "organization_recommendation" in value:
        import capo_trustedadvisor.types.organization_recommendation

        out["organization_recommendation"] = (
            capo_trustedadvisor.types.organization_recommendation.redact_sensitive(
                value["organization_recommendation"]
            )
        )
    return out
