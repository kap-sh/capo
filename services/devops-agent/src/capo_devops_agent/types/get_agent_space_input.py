"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id


class GetAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentSpaceInput:
    out: GetAgentSpaceInput = {}  # type: ignore[typeddict-item]
    return out
