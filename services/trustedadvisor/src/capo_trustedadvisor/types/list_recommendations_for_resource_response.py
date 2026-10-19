"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_for_resource_summary_list


class ListRecommendationsForResourceResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    recommendation_for_resource_summaries: "capo_trustedadvisor.types.recommendation_for_resource_summary_list.RecommendationForResourceSummaryList"
    """<p>List of Trusted Advisor recommendations associated with the given AWS resource</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsForResourceResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.recommendation_for_resource_summary_list

    out["recommendationForResourceSummaries"] = (
        capo_trustedadvisor.types.recommendation_for_resource_summary_list.serialize_json(
            value["recommendation_for_resource_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRecommendationsForResourceResponse:
    out: ListRecommendationsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationForResourceSummaries") is not None:
        import capo_trustedadvisor.types.recommendation_for_resource_summary_list

        out["recommendation_for_resource_summaries"] = (
            capo_trustedadvisor.types.recommendation_for_resource_summary_list.deserialize_json(
                data["recommendationForResourceSummaries"]
            )
        )
    else:
        out["recommendation_for_resource_summaries"] = []
    return out
