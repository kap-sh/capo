"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeEndpointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.endpoint_name


class DeleteAgentRuntimeEndpointResponse(TypedDict, closed=True):
    status: "capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the AgentCore Runtime endpoint deletion.</p>"""
    agent_runtime_id: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    ]
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    endpoint_name: NotRequired[
        "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    ]
    """<p>The name of the AgentCore Runtime endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeEndpointResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(
            value["status"]
        )
    )
    if "agent_runtime_id" in value:
        out["agentRuntimeId"] = value["agent_runtime_id"]
    if "endpoint_name" in value:
        out["endpointName"] = value["endpoint_name"]
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeEndpointResponse:
    out: DeleteAgentRuntimeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteAgentRuntimeEndpointResponse.status required")
    if data.get("agentRuntimeId") is not None:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    return out


def redact_sensitive(value: DeleteAgentRuntimeEndpointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoint_name" in value:
        out["endpoint_name"] = "*** Sensitive Data Redacted ***"
    return out
