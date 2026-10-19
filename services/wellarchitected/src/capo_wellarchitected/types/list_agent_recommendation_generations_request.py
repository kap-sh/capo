"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.recommendation_type


class ListAgentRecommendationGenerationsRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to list generation processes for.</p>"""
    recommendation_type: NotRequired[
        "capo_wellarchitected.types.recommendation_type.RecommendationType"
    ]
    """<p>Optional filter by recommendation type.</p>"""
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>The maximum number of generation processes to return in a single response.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to continue retrieving results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationGenerationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationGenerationsRequest:
    out: ListAgentRecommendationGenerationsRequest = {}  # type: ignore[typeddict-item]
    return out
