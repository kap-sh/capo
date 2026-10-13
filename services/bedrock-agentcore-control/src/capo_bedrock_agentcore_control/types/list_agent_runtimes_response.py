"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtimes
    import capo_bedrock_agentcore_control.types.next_token


class ListAgentRuntimesResponse(TypedDict, closed=True):
    agent_runtimes: "capo_bedrock_agentcore_control.types.agent_runtimes.AgentRuntimes"
    """<p>The list of AgentCore Runtime resources.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.agent_runtimes

    out["agentRuntimes"] = (
        capo_bedrock_agentcore_control.types.agent_runtimes.serialize_json(
            value["agent_runtimes"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRuntimesResponse:
    out: ListAgentRuntimesResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentRuntimes") is not None:
        import capo_bedrock_agentcore_control.types.agent_runtimes

        out["agent_runtimes"] = (
            capo_bedrock_agentcore_control.types.agent_runtimes.deserialize_json(
                data["agentRuntimes"]
            )
        )
    else:
        raise DeserializationError("ListAgentRuntimesResponse.agent_runtimes required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAgentRuntimesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_runtimes" in value:
        import capo_bedrock_agentcore_control.types.agent_runtimes

        out["agent_runtimes"] = (
            capo_bedrock_agentcore_control.types.agent_runtimes.redact_sensitive(
                value["agent_runtimes"]
            )
        )
    return out
