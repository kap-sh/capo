"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPolicyGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.resource_id


class GetPolicyGenerationRequest(TypedDict, closed=True):
    policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html">StartPolicyGeneration</a> call.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyGenerationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyGenerationRequest:
    out: GetPolicyGenerationRequest = {}  # type: ignore[typeddict-item]
    return out
