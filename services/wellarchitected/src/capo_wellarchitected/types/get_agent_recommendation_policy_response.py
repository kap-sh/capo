"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_arn
    import capo_wellarchitected.types.resource_policy


class GetAgentRecommendationPolicyResponse(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.agent_recommendation_arn.AgentRecommendationArn"
    )
    """<p>The ARN of the Agent Recommendation.</p>"""
    policy: "capo_wellarchitected.types.resource_policy.ResourcePolicy"
    """<p>The IAM resource-based policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationPolicyResponse) -> dict:
    out: dict = {}
    out["recommendationArn"] = value["recommendation_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationPolicyResponse:
    out: GetAgentRecommendationPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
