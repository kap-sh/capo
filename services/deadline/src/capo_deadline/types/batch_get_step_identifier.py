"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id


class BatchGetStepIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the step."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the step."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the step."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> BatchGetStepIdentifier:
    out: BatchGetStepIdentifier = {}  # type: ignore[typeddict-item]
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
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        out["step_id"] = ""
    return out
