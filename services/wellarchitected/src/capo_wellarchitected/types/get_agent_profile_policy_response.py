"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentProfilePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.resource_policy


class GetAgentProfilePolicyResponse(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The ARN of the Agent Profile.</p>"""
    policy: "capo_wellarchitected.types.resource_policy.ResourcePolicy"
    """<p>The IAM resource-based policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentProfilePolicyResponse) -> dict:
    out: dict = {}
    out["profileArn"] = value["profile_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetAgentProfilePolicyResponse:
    out: GetAgentProfilePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
