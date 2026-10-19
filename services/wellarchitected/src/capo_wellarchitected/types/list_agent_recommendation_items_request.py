"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentRecommendationItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.recommendation_item_type


class ListAgentRecommendationItemsRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation to list items for.</p>"""
    type: NotRequired[
        "capo_wellarchitected.types.recommendation_item_type.RecommendationItemType"
    ]
    """<p>Optional filter to return only recommendation items of the specified type.</p>"""
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>The maximum number of recommendation items to return in a single response.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to continue retrieving results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRecommendationItemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentRecommendationItemsRequest:
    out: ListAgentRecommendationItemsRequest = {}  # type: ignore[typeddict-item]
    return out
