"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn


class GetAgentRecommendationPolicyRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The ARN of the Agent Recommendation whose policy to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationPolicyRequest:
    out: GetAgentRecommendationPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
