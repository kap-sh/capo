"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_action_id


class BatchGetSessionActionIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the session action.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the session action.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID of the session action.</p>"""
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["sessionActionId"] = value["session_action_id"]
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionIdentifier:
    out: BatchGetSessionActionIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("sessionActionId") is not None:
        out["session_action_id"] = data["sessionActionId"]
    else:
        out["session_action_id"] = ""
    return out
