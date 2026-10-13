"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAgentSpaceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space
    import capo_devops_agent.types.tags


class GetAgentSpaceOutput(TypedDict, closed=True):
    agent_space: "capo_devops_agent.types.agent_space.AgentSpace"
    tags: NotRequired["capo_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the AgentSpace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentSpaceOutput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.agent_space

    out["agentSpace"] = capo_devops_agent.types.agent_space.serialize_json(
        value["agent_space"]
    )
    if "tags" in value:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetAgentSpaceOutput:
    out: GetAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpace") is not None:
        import capo_devops_agent.types.agent_space

        out["agent_space"] = capo_devops_agent.types.agent_space.deserialize_json(
            data["agentSpace"]
        )
    else:
        raise DeserializationError("GetAgentSpaceOutput.agent_space required")
    if data.get("tags") is not None:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetAgentSpaceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_space" in value:
        import capo_devops_agent.types.agent_space

        out["agent_space"] = capo_devops_agent.types.agent_space.redact_sensitive(
            value["agent_space"]
        )
    return out
