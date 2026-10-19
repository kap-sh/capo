"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_resource_summary_list


class ListRecommendationResourcesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    recommendation_resource_summaries: "capo_trustedadvisor.types.recommendation_resource_summary_list.RecommendationResourceSummaryList"
    """<p>A list of Recommendation Resources</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationResourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.recommendation_resource_summary_list

    out["recommendationResourceSummaries"] = (
        capo_trustedadvisor.types.recommendation_resource_summary_list.serialize_json(
            value["recommendation_resource_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRecommendationResourcesResponse:
    out: ListRecommendationResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationResourceSummaries") is not None:
        import capo_trustedadvisor.types.recommendation_resource_summary_list

        out["recommendation_resource_summaries"] = (
            capo_trustedadvisor.types.recommendation_resource_summary_list.deserialize_json(
                data["recommendationResourceSummaries"]
            )
        )
    else:
        out["recommendation_resource_summaries"] = []
    return out
