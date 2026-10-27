"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id
    import capo_deadline.types.task_target_run_status


class BatchUpdateTaskItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the task to update."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the task to update."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the task to update."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID of the task to update."""
    task_id: "capo_deadline.types.task_id.TaskId"
    """The task ID of the task to update."""
    target_run_status: "capo_deadline.types.task_target_run_status.TaskTargetRunStatus"
    """The run status with which to start the task."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    import capo_deadline.types.task_target_run_status

    out["targetRunStatus"] = capo_deadline.types.task_target_run_status.serialize_json(
        value["target_run_status"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskItem:
    out: BatchUpdateTaskItem = {}  # type: ignore[typeddict-item]
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
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("targetRunStatus") is not None:
        import capo_deadline.types.task_target_run_status

        out["target_run_status"] = (
            capo_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    else:
        import typing

        out["target_run_status"] = typing.cast(
            "capo_deadline.types.task_target_run_status.TaskTargetRunStatus", ""
        )
    return out
