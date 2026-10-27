"""Generated from Smithy shape ``com.amazonaws.deadline#GetTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id


class GetTaskRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm connected to the task."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the queue connected to the task."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the job connected to the task."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID for the step connected to the task."""
    task_id: "capo_deadline.types.task_id.TaskId"
    """The task ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTaskRequest:
    out: GetTaskRequest = {}  # type: ignore[typeddict-item]
    return out
