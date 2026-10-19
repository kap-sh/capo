"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentTaskResponseUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class GetAgentTaskResponseUrlResponse(TypedDict, closed=True):
    agent_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of the agent.</p>"""
    task_id: "capo_groundstation.types.uuid.Uuid"
    """<p>GUID of the agent task.</p>"""
    presigned_log_url: "str"
    """<p>Presigned URL for uploading agent task response logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentTaskResponseUrlResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["taskId"] = value["task_id"]
    out["presignedLogUrl"] = value["presigned_log_url"]
    return out


def deserialize_json(data: dict) -> GetAgentTaskResponseUrlResponse:
    out: GetAgentTaskResponseUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    else:
        out["agent_id"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("presignedLogUrl") is not None:
        out["presigned_log_url"] = data["presignedLogUrl"]
    else:
        out["presigned_log_url"] = ""
    return out
