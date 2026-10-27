"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_task_error_code
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id
    import capo_deadline.types.string
    import capo_deadline.types.task_id


class BatchUpdateTaskError(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the task that could not be updated."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the task that could not be updated."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the task that could not be updated."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID of the task that could not be updated."""
    task_id: "capo_deadline.types.task_id.TaskId"
    """The task ID of the task that could not be updated."""
    code: "capo_deadline.types.batch_update_task_error_code.BatchUpdateTaskErrorCode"
    """The error code."""
    message: "capo_deadline.types.string.String"
    """The error message."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    import capo_deadline.types.batch_update_task_error_code

    out["code"] = capo_deadline.types.batch_update_task_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskError:
    out: BatchUpdateTaskError = {}  # type: ignore[typeddict-item]
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
    if data.get("code") is not None:
        import capo_deadline.types.batch_update_task_error_code

        out["code"] = capo_deadline.types.batch_update_task_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_deadline.types.batch_update_task_error_code.BatchUpdateTaskErrorCode",
            "",
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
