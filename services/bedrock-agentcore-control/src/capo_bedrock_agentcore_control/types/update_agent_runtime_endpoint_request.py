"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_endpoint_description
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.endpoint_name


class UpdateAgentRuntimeEndpointRequest(TypedDict, closed=True):
    agent_runtime_id: (
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to update.</p>"""
    agent_runtime_version: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The updated version of the AgentCore Runtime for the endpoint.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
    ]
    """<p>The updated description of the AgentCore Runtime endpoint.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    if "agent_runtime_version" in value:
        out["agentRuntimeVersion"] = value["agent_runtime_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAgentRuntimeEndpointRequest:
    out: UpdateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimeVersion") is not None:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateAgentRuntimeEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_name" in value:
        out["endpoint_name"] = "*** Sensitive Data Redacted ***"
    return out
