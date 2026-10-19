"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.organization_recommendation_summary_list


class ListOrganizationRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    organization_recommendation_summaries: "capo_trustedadvisor.types.organization_recommendation_summary_list.OrganizationRecommendationSummaryList"
    """<p>The list of Recommendations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.organization_recommendation_summary_list

    out["organizationRecommendationSummaries"] = (
        capo_trustedadvisor.types.organization_recommendation_summary_list.serialize_json(
            value["organization_recommendation_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationsResponse:
    out: ListOrganizationRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("organizationRecommendationSummaries") is not None:
        import capo_trustedadvisor.types.organization_recommendation_summary_list

        out["organization_recommendation_summaries"] = (
            capo_trustedadvisor.types.organization_recommendation_summary_list.deserialize_json(
                data["organizationRecommendationSummaries"]
            )
        )
    else:
        out["organization_recommendation_summaries"] = []
    return out
