"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_item_summaries
    import capo_wellarchitected.types.next_token


class ListAgentRecommendationItemsResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.agent_recommendation_item_summaries.AgentRecommendationItemSummaries"
    """<p>A list of recommendation items with their detailed metadata and configuration information.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next set of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationItemsResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.agent_recommendation_item_summaries

    out["items"] = (
        capo_wellarchitected.types.agent_recommendation_item_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationItemsResponse:
    out: ListAgentRecommendationItemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.agent_recommendation_item_summaries

        out["items"] = (
            capo_wellarchitected.types.agent_recommendation_item_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
