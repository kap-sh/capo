"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentActionGroupResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_action_group


class GetAgentActionGroupResponse(TypedDict, closed=True):
    agent_action_group: "capo_bedrock_agent.types.agent_action_group.AgentActionGroup"
    """<p>Contains details about the action group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentActionGroupResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_action_group

    out["agentActionGroup"] = (
        capo_bedrock_agent.types.agent_action_group.serialize_json(
            value["agent_action_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAgentActionGroupResponse:
    out: GetAgentActionGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentActionGroup") is not None:
        import capo_bedrock_agent.types.agent_action_group

        out["agent_action_group"] = (
            capo_bedrock_agent.types.agent_action_group.deserialize_json(
                data["agentActionGroup"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentActionGroupResponse.agent_action_group required"
        )
    return out


def redact_sensitive(value: GetAgentActionGroupResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_action_group" in value:
        import capo_bedrock_agent.types.agent_action_group

        out["agent_action_group"] = (
            capo_bedrock_agent.types.agent_action_group.redact_sensitive(
                value["agent_action_group"]
            )
        )
    return out
