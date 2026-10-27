"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id


class BatchGetJobIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the job."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the job."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> BatchGetJobIdentifier:
    out: BatchGetJobIdentifier = {}  # type: ignore[typeddict-item]
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
    return out
