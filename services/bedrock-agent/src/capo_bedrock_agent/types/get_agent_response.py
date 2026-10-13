"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent


class GetAgentResponse(TypedDict, closed=True):
    agent: "capo_bedrock_agent.types.agent.Agent"
    """<p>Contains details about the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent

    out["agent"] = capo_bedrock_agent.types.agent.serialize_json(value["agent"])
    return out


def deserialize_json(data: dict) -> GetAgentResponse:
    out: GetAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("agent") is not None:
        import capo_bedrock_agent.types.agent

        out["agent"] = capo_bedrock_agent.types.agent.deserialize_json(data["agent"])
    else:
        raise DeserializationError("GetAgentResponse.agent required")
    return out


def redact_sensitive(value: GetAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent" in value:
        import capo_bedrock_agent.types.agent

        out["agent"] = capo_bedrock_agent.types.agent.redact_sensitive(value["agent"])
    return out
