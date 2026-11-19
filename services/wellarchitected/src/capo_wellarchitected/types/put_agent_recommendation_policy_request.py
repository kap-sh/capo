"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PutAgentRecommendationPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.resource_policy


class PutAgentRecommendationPolicyRequest(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The ARN of the Agent Recommendation to attach the policy to.</p>"""
    policy: "capo_wellarchitected.types.resource_policy.ResourcePolicy"
    """<p>The IAM resource-based policy document in JSON format. Maximum size 50KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAgentRecommendationPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutAgentRecommendationPolicyRequest:
    out: PutAgentRecommendationPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
