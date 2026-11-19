"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PutAgentProfilePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.resource_policy


class PutAgentProfilePolicyRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The ARN of the Agent Profile to attach the policy to.</p>"""
    policy: "capo_wellarchitected.types.resource_policy.ResourcePolicy"
    """<p>The IAM resource-based policy document in JSON format. Maximum size 50KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAgentProfilePolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutAgentProfilePolicyRequest:
    out: PutAgentProfilePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
