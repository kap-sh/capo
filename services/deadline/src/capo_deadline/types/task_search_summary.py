"""Generated from Smithy shape ``com.amazonaws.deadline#TaskSearchSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ended_at
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


class TaskSearchSummary(TypedDict, closed=True):
    task_id: NotRequired["capo_deadline.types.task_id.TaskId"]
    """<p>The task ID.</p>"""
    step_id: NotRequired["capo_deadline.types.step_id.StepId"]
    """<p>The step ID.</p>"""
    job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """<p>The job ID.</p>"""
    queue_id: NotRequired["capo_deadline.types.queue_id.QueueId"]
    """<p>The queue ID.</p>"""
    run_status: NotRequired["capo_deadline.types.task_run_status.TaskRunStatus"]
    """<p>The run status of the task.</p>"""
    target_run_status: NotRequired[
        "capo_deadline.types.task_target_run_status.TaskTargetRunStatus"
    ]
    """<p>The run status that the task is being updated to.</p>"""
    parameters: NotRequired["capo_deadline.types.task_parameters.TaskParameters"]
    """<p>The parameters to search for.</p>"""
    failure_retry_count: NotRequired[
        "capo_deadline.types.task_retry_count.TaskRetryCount"
    ]
    """<p>The number of times that the task failed and was retried.</p>"""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    latest_session_action_id: NotRequired[
        "capo_deadline.types.session_action_id.SessionActionId"
    ]
    """<p>The latest session action ID for the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskSearchSummary) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "run_status" in value:
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
    if "parameters" in value:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.serialize_json(
            value["parameters"]
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
    return out


def deserialize_json(data: dict) -> TaskSearchSummary:
    out: TaskSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    if data.get("runStatus") is not None:
        import capo_deadline.types.task_run_status

        out["run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["runStatus"]
        )
    if data.get("targetRunStatus") is not None:
        import capo_deadline.types.task_target_run_status

        out["target_run_status"] = (
            capo_deadline.types.task_target_run_status.deserialize_json(
                data["targetRunStatus"]
            )
        )
    if data.get("parameters") is not None:
        import capo_deadline.types.task_parameters

        out["parameters"] = capo_deadline.types.task_parameters.deserialize_json(
            data["parameters"]
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
    return out


def redact_sensitive(value: TaskSearchSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
