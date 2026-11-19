"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteAgentRecommendationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn


class DeleteAgentRecommendationPolicyRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The ARN of the Agent Recommendation whose policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRecommendationPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentRecommendationPolicyRequest:
    out: DeleteAgentRecommendationPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
