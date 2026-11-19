"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetChatRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.resource_id


class GetChatRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The unique identifier of the agent space that contains the chat execution.</p>"""
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the chat execution to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChatRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChatRequest:
    out: GetChatRequest = {}  # type: ignore[typeddict-item]
    return out
