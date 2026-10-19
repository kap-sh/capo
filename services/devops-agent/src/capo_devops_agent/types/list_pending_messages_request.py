"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPendingMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.resource_id


class ListPendingMessagesRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    execution_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the execution whose journal records to retrieve</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMessagesRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> ListPendingMessagesRequest:
    out: ListPendingMessagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    return out
