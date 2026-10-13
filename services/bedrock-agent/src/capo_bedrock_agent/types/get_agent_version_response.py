"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_version


class GetAgentVersionResponse(TypedDict, closed=True):
    agent_version: "capo_bedrock_agent.types.agent_version.AgentVersion"
    """<p>Contains details about the version of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentVersionResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_version

    out["agentVersion"] = capo_bedrock_agent.types.agent_version.serialize_json(
        value["agent_version"]
    )
    return out


def deserialize_json(data: dict) -> GetAgentVersionResponse:
    out: GetAgentVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentVersion") is not None:
        import capo_bedrock_agent.types.agent_version

        out["agent_version"] = capo_bedrock_agent.types.agent_version.deserialize_json(
            data["agentVersion"]
        )
    else:
        raise DeserializationError("GetAgentVersionResponse.agent_version required")
    return out


def redact_sensitive(value: GetAgentVersionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_version" in value:
        import capo_bedrock_agent.types.agent_version

        out["agent_version"] = capo_bedrock_agent.types.agent_version.redact_sensitive(
            value["agent_version"]
        )
    return out
