"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.endpoint_name


class DeleteAgentRuntimeEndpointRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to delete.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeEndpointRequest:
    out: DeleteAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: DeleteAgentRuntimeEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_name" in value:
        out["endpoint_name"] = "*** Sensitive Data Redacted ***"
    return out
