"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteAgentProfilePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn


class DeleteAgentProfilePolicyRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The ARN of the Agent Profile whose policy to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentProfilePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentProfilePolicyRequest:
    out: DeleteAgentProfilePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
