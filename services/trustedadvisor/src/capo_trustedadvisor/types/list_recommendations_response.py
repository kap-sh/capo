"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.recommendation_summary_list


class ListRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    recommendation_summaries: "capo_trustedadvisor.types.recommendation_summary_list.RecommendationSummaryList"
    """<p>The list of Recommendations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.recommendation_summary_list

    out["recommendationSummaries"] = (
        capo_trustedadvisor.types.recommendation_summary_list.serialize_json(
            value["recommendation_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("recommendationSummaries") is not None:
        import capo_trustedadvisor.types.recommendation_summary_list

        out["recommendation_summaries"] = (
            capo_trustedadvisor.types.recommendation_summary_list.deserialize_json(
                data["recommendationSummaries"]
            )
        )
    else:
        out["recommendation_summaries"] = []
    return out
