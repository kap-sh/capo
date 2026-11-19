"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentProfilePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn


class GetAgentProfilePolicyRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The ARN of the Agent Profile whose policy to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentProfilePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentProfilePolicyRequest:
    out: GetAgentProfilePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
