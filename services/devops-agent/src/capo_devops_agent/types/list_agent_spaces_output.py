"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAgentSpacesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_list
    import capo_devops_agent.types.next_token


class ListAgentSpacesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    agent_spaces: "capo_devops_agent.types.agent_space_list.AgentSpaceList"
    """<p>The list of AgentSpaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentSpacesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_devops_agent.types.agent_space_list

    out["agentSpaces"] = capo_devops_agent.types.agent_space_list.serialize_json(
        value["agent_spaces"]
    )
    return out


def deserialize_json(data: dict) -> ListAgentSpacesOutput:
    out: ListAgentSpacesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("agentSpaces") is not None:
        import capo_devops_agent.types.agent_space_list

        out["agent_spaces"] = capo_devops_agent.types.agent_space_list.deserialize_json(
            data["agentSpaces"]
        )
    else:
        raise DeserializationError("ListAgentSpacesOutput.agent_spaces required")
    return out


def redact_sensitive(value: ListAgentSpacesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_spaces" in value:
        import capo_devops_agent.types.agent_space_list

        out["agent_spaces"] = capo_devops_agent.types.agent_space_list.redact_sensitive(
            value["agent_spaces"]
        )
    return out
