"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation_resource_summary_list


class ListOrganizationRecommendationResourcesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    organization_recommendation_resource_summaries: "capo_trustedadvisor.types.organization_recommendation_resource_summary_list.OrganizationRecommendationResourceSummaryList"
    """<p>A list of Recommendation Resources</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationResourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.organization_recommendation_resource_summary_list

    out["organizationRecommendationResourceSummaries"] = (
        capo_trustedadvisor.types.organization_recommendation_resource_summary_list.serialize_json(
            value["organization_recommendation_resource_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationResourcesResponse:
    out: ListOrganizationRecommendationResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("organizationRecommendationResourceSummaries") is not None:
        import capo_trustedadvisor.types.organization_recommendation_resource_summary_list

        out["organization_recommendation_resource_summaries"] = (
            capo_trustedadvisor.types.organization_recommendation_resource_summary_list.deserialize_json(
                data["organizationRecommendationResourceSummaries"]
            )
        )
    else:
        out["organization_recommendation_resource_summaries"] = []
    return out
