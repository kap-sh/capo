"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent


class UpdateAgentResponse(TypedDict, closed=True):
    agent: "capo_bedrock_agent.types.agent.Agent"
    """<p>Contains details about the agent that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent

    out["agent"] = capo_bedrock_agent.types.agent.serialize_json(value["agent"])
    return out


def deserialize_json(data: dict) -> UpdateAgentResponse:
    out: UpdateAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("agent") is not None:
        import capo_bedrock_agent.types.agent

        out["agent"] = capo_bedrock_agent.types.agent.deserialize_json(data["agent"])
    else:
        raise DeserializationError("UpdateAgentResponse.agent required")
    return out


def redact_sensitive(value: UpdateAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent" in value:
        import capo_bedrock_agent.types.agent

        out["agent"] = capo_bedrock_agent.types.agent.redact_sensitive(value["agent"])
    return out
