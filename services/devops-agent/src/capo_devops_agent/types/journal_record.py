"""Generated from Smithy shape ``com.amazonaws.devopsagent#JournalRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.journal_timestamp
    import capo_devops_agent.types.user_reference


class JournalRecord(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier for the agent space containing this record</p>"""
    execution_id: "str"
    """<p>The execution ID associated with this journal record</p>"""
    record_id: "str"
    """<p>The unique identifier for this journal record</p>"""
    content: "object"
    """<p>The content of this journal record</p>"""
    created_at: "capo_devops_agent.types.journal_timestamp.JournalTimestamp"
    """<p>Timestamp when this journal record was created</p>"""
    record_type: "str"
    """<p>The type of this journal record</p>"""
    user_reference: NotRequired["capo_devops_agent.types.user_reference.UserReference"]
    """<p>Reference to the user associated with this journal record</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JournalRecord) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["executionId"] = value["execution_id"]
    out["recordId"] = value["record_id"]
    out["content"] = value["content"]
    import capo_devops_agent.types.journal_timestamp

    out["createdAt"] = capo_devops_agent.types.journal_timestamp.serialize_json(
        value["created_at"]
    )
    out["recordType"] = value["record_type"]
    if "user_reference" in value:
        import capo_devops_agent.types.user_reference

        out["userReference"] = capo_devops_agent.types.user_reference.serialize_json(
            value["user_reference"]
        )
    return out


def deserialize_json(data: dict) -> JournalRecord:
    out: JournalRecord = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        out["record_id"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = None
    if data.get("createdAt") is not None:
        import capo_devops_agent.types.journal_timestamp

        out["created_at"] = capo_devops_agent.types.journal_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("recordType") is not None:
        out["record_type"] = data["recordType"]
    else:
        out["record_type"] = ""
    if data.get("userReference") is not None:
        import capo_devops_agent.types.user_reference

        out["user_reference"] = capo_devops_agent.types.user_reference.deserialize_json(
            data["userReference"]
        )
    return out
