"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.ended_at
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_action_id
    import capo_deadline.types.started_at
    import capo_deadline.types.step_id
    import capo_deadline.types.task_id
    import capo_deadline.types.task_parameters
    import capo_deadline.types.task_retry_count
    import capo_deadline.types.task_run_status
    import capo_deadline.types.task_target_run_status
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class BatchGetTaskItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the task."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the task."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the task."""
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID of the task."""
    task_id: "capo_deadline.types.task_id.TaskId"
    """The task ID."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The date and time the resource was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user or system that created this resource."""
    run_status: "capo_deadline.types.task_run_status.TaskRunStatus"
    """The run status of the task."""
    target_run_status: NotRequired[
        "capo_deadline.types.task_target_run_status.TaskTargetRunStatus"
    ]
    """The run status with which to start the task."""
    failure_retry_count: NotRequired[
        "capo_deadline.types.task_retry_count.TaskRetryCount"
    ]
    """The number of times the task failed and was retried."""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """The date and time the resource started running."""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """The date and time the resource ended running."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""
    latest_session_action_id: NotRequired[
        "capo_deadline.types.session_action_id.SessionActionId"
    ]
    """The latest session action for the task."""
    parameters: NotRequired["capo_deadline.types.task_parameters.TaskParameters"]
    """The parameters for the task."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["stepId"] = value["step_id"]
    out["taskId"] = value["task_id"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    import capo_deadline.types.task_run_status

    out["runStatus"] = capo_deadline.types.task_run_status.serialize_json(
        value["run_status"]
    )
    if "target_run_status" in value:
        import capo_deadline.types.task_target_run_status

        out["targetRunStatus"] = (
            capo_deadline.types.task_target_run_status.serialize_json(
                value["target_run_status"]
            )
        )
    if "failure_retry_count" in value:
        out["failureRetryCount"] = value["failure_retry_count"]
    if "started_at" in value:
        import capo_deadline.types.started_at

        out["startedAt"] = capo_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "latest_session_action_id" in value:
        out["latestSessionActionId"] = value["latest_session_action_id"]
    if "parameters" in value:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetTaskItem:
    out: BatchGetTaskItem = {}  # type: ignore[typeddict-item]
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
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("runStatus") is not None:
        import capo_deadline.types.task_run_status

        out["run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["runStatus"]
        )
    else:
        import typing

        out["run_status"] = typing.cast(
            "capo_deadline.types.task_run_status.TaskRunStatus", ""
        )
    if data.get("targetRunStatus") is not None:
        import capo_deadline.types.task_target_run_status

        out["target_run_status"] = (
            capo_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    if data.get("failureRetryCount") is not None:
        out["failure_retry_count"] = data["failureRetryCount"]
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("latestSessionActionId") is not None:
        out["latest_session_action_id"] = data["latestSessionActionId"]
    if data.get("parameters") is not None:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
        )
    return out


def redact_sensitive(value: BatchGetTaskItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
