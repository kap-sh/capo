"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.endpoint_name


class GetAgentRuntimeEndpointRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeEndpointRequest:
    out: GetAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetAgentRuntimeEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_name" in value:
        out["endpoint_name"] = "*** Sensitive Data Redacted ***"
    return out
