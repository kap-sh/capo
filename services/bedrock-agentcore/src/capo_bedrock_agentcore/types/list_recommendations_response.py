"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.recommendation_summary_list


class ListRecommendationsResponse(TypedDict, closed=True):
    recommendation_summaries: "capo_bedrock_agentcore.types.recommendation_summary_list.RecommendationSummaryList"
    """<p>The list of recommendation summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.recommendation_summary_list

    out["recommendationSummaries"] = (
        capo_bedrock_agentcore.types.recommendation_summary_list.serialize_json(
            value["recommendation_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationSummaries") is not None:
        import capo_bedrock_agentcore.types.recommendation_summary_list

        out["recommendation_summaries"] = (
            capo_bedrock_agentcore.types.recommendation_summary_list.deserialize_json(
                data["recommendationSummaries"]
            )
        )
    else:
        out["recommendation_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
