"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimeEndpointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoints
    import capo_bedrock_agentcore_control.types.next_token


class ListAgentRuntimeEndpointsResponse(TypedDict, closed=True):
    runtime_endpoints: "capo_bedrock_agentcore_control.types.agent_runtime_endpoints.AgentRuntimeEndpoints"
    """<p>The list of AgentCore Runtime endpoints.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimeEndpointsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoints

    out["runtimeEndpoints"] = (
        capo_bedrock_agentcore_control.types.agent_runtime_endpoints.serialize_json(
            value["runtime_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRuntimeEndpointsResponse:
    out: ListAgentRuntimeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("runtimeEndpoints") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtime_endpoints

        out["runtime_endpoints"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_endpoints.deserialize_json(
                data["runtimeEndpoints"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgentRuntimeEndpointsResponse.runtime_endpoints required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentRuntimeEndpointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "runtime_endpoints" in value:
        import capo_bedrock_agentcore_control.types.agent_runtime_endpoints

        out["runtime_endpoints"] = (
            capo_bedrock_agentcore_control.types.agent_runtime_endpoints.redact_sensitive(
                value["runtime_endpoints"]
            )
        )
    return out
