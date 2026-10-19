"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationGenerationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_generation_summaries
    import capo_wellarchitected.types.next_token


class ListAgentRecommendationGenerationsResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.agent_recommendation_generation_summaries.AgentRecommendationGenerationSummaries"
    """<p>A list of recommendation generation summaries.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next set of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationGenerationsResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.agent_recommendation_generation_summaries

    out["items"] = (
        capo_wellarchitected.types.agent_recommendation_generation_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationGenerationsResponse:
    out: ListAgentRecommendationGenerationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.agent_recommendation_generation_summaries

        out["items"] = (
            capo_wellarchitected.types.agent_recommendation_generation_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
