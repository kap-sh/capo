"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_summaries
    import capo_wellarchitected.types.next_token


class ListAgentRecommendationsResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.agent_recommendation_summaries.AgentRecommendationSummaries"
    """<p>A list of recommendation summaries.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token to retrieve the next set of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationsResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.agent_recommendation_summaries

    out["items"] = (
        capo_wellarchitected.types.agent_recommendation_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationsResponse:
    out: ListAgentRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.agent_recommendation_summaries

        out["items"] = (
            capo_wellarchitected.types.agent_recommendation_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentRecommendationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_wellarchitected.types.agent_recommendation_summaries

        out["items"] = (
            capo_wellarchitected.types.agent_recommendation_summaries.redact_sensitive(
                value["items"]
            )
        )
    return out
