"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPendingMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.pending_messages


class ListPendingMessagesResponse(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    execution_id: "str"
    """<p>The unique identifier for the execution.</p>"""
    messages: "capo_devops_agent.types.pending_messages.PendingMessages"
    """<p>The list of pending messages for the execution.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the pending messages were created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMessagesResponse) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["executionId"] = value["execution_id"]
    import capo_devops_agent.types.pending_messages

    out["messages"] = capo_devops_agent.types.pending_messages.serialize_json(
        value.get("messages", [])
    )
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> ListPendingMessagesResponse:
    out: ListPendingMessagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("messages") is not None:
        import capo_devops_agent.types.pending_messages

        out["messages"] = capo_devops_agent.types.pending_messages.deserialize_json(
            data["messages"]
        )
    else:
        out["messages"] = []
    if data.get("createdAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
