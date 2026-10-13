"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpaceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space

AgentSpaceList: TypeAlias = list["capo_devops_agent.types.agent_space.AgentSpace"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceList) -> list:
    import capo_devops_agent.types.agent_space

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.agent_space.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentSpaceList:
    import capo_devops_agent.types.agent_space

    out: AgentSpaceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_devops_agent.types.agent_space.deserialize_json(item))
    return out


def redact_sensitive(value: AgentSpaceList) -> list[Any]:
    import capo_devops_agent.types.agent_space

    return [
        capo_devops_agent.types.agent_space.redact_sensitive(item) for item in value
    ]
