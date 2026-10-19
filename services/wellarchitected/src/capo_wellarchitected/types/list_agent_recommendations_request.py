"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.pillar
    import capo_wellarchitected.types.recommendation_state


class ListAgentRecommendationsRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to list recommendations for.</p>"""
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>The maximum number of recommendations to return in a single response.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to continue retrieving results.</p>"""
    state: NotRequired[
        "capo_wellarchitected.types.recommendation_state.RecommendationState"
    ]
    """<p>Optional filter to return only recommendations with the specified state (OPEN or CLOSED).</p>"""
    pillar: NotRequired["capo_wellarchitected.types.pillar.Pillar"]
    """<p>Optional filter to return only recommendations for the specified pillar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationsRequest:
    out: ListAgentRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
