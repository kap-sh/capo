"""Generated from Smithy shape ``com.amazonaws.deadline#StepSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.ended_at
    import capo_deadline.types.job_id
    import capo_deadline.types.parameter_space
    import capo_deadline.types.queue_id
    import capo_deadline.types.started_at
    import capo_deadline.types.step_id
    import capo_deadline.types.step_lifecycle_status
    import capo_deadline.types.step_name
    import capo_deadline.types.step_target_task_run_status
    import capo_deadline.types.string
    import capo_deadline.types.task_failure_retry_count
    import capo_deadline.types.task_run_status
    import capo_deadline.types.task_run_status_counts
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class StepSearchSummary(TypedDict, closed=True):
    step_id: NotRequired["capo_deadline.types.step_id.StepId"]
    """The step ID."""
    job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """The job ID."""
    queue_id: NotRequired["capo_deadline.types.queue_id.QueueId"]
    """The queue ID."""
    name: NotRequired["capo_deadline.types.step_name.StepName"]
    """The step name."""
    lifecycle_status: NotRequired[
        "capo_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    ]
    """The life cycle status."""
    lifecycle_status_message: NotRequired["capo_deadline.types.string.String"]
    """The life cycle status message."""
    task_run_status: NotRequired["capo_deadline.types.task_run_status.TaskRunStatus"]
    """<p>The task run status for the job.</p> <ul> <li> <p> <code>PENDING</code>–pending and waiting for resources.</p> </li> <li> <p> <code>READY</code>–ready to be processed.</p> </li> <li> <p> <code>ASSIGNED</code>–assigned and will run next on a worker.</p> </li> <li> <p> <code>SCHEDULED</code>–scheduled to be run on a worker.</p> </li> <li> <p> <code>INTERRUPTING</code>–being interrupted.</p> </li> <li> <p> <code>RUNNING</code>–running on a worker.</p> </li> <li> <p> <code>SUSPENDED</code>–the task is suspended.</p> </li> <li> <p> <code>CANCELED</code>–the task has been canceled.</p> </li> <li> <p> <code>FAILED</code>–the task has failed.</p> </li> <li> <p> <code>SUCCEEDED</code>–the task has succeeded.</p> </li> </ul>"""
    target_task_run_status: NotRequired[
        "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """The task status to update the job's tasks to."""
    task_run_status_counts: NotRequired[
        "capo_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    ]
    """The number of tasks running on the job."""
    task_failure_retry_count: NotRequired[
        "capo_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """The total number of times tasks from the step failed and were retried."""
    created_at: NotRequired["capo_deadline.types.created_at.CreatedAt"]
    """The date and time the resource was created."""
    created_by: NotRequired["capo_deadline.types.created_by.CreatedBy"]
    """The user or system that created this resource."""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """The date and time the resource started running."""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """The date and time the resource ended running."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""
    parameter_space: NotRequired["capo_deadline.types.parameter_space.ParameterSpace"]
    """The parameters and combination expressions for the search."""


# --- restJson1 ser/de ---
def serialize_json(value: StepSearchSummary) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "lifecycle_status" in value:
        import capo_deadline.types.step_lifecycle_status

        out["lifecycleStatus"] = (
            capo_deadline.types.step_lifecycle_status.serialize_json(
                value["lifecycle_status"]
            )
        )
    if "lifecycle_status_message" in value:
        out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    if "task_run_status" in value:
        import capo_deadline.types.task_run_status

        out["taskRunStatus"] = capo_deadline.types.task_run_status.serialize_json(
            value["task_run_status"]
        )
    if "target_task_run_status" in value:
        import capo_deadline.types.step_target_task_run_status

        out["targetTaskRunStatus"] = (
            capo_deadline.types.step_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    if "task_run_status_counts" in value:
        import capo_deadline.types.task_run_status_counts

        out["taskRunStatusCounts"] = (
            capo_deadline.types.task_run_status_counts.serialize_json(
                value["task_run_status_counts"]
            )
        )
    if "task_failure_retry_count" in value:
        out["taskFailureRetryCount"] = value["task_failure_retry_count"]
    if "created_at" in value:
        import capo_deadline.types.created_at

        out["createdAt"] = capo_deadline.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
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
    if "parameter_space" in value:
        import capo_deadline.types.parameter_space

        out["parameterSpace"] = capo_deadline.types.parameter_space.serialize_json(
            value["parameter_space"]
        )
    return out


def deserialize_json(data: dict) -> StepSearchSummary:
    out: StepSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    if data.get("lifecycleStatusMessage") is not None:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    if data.get("taskRunStatus") is not None:
        import capo_deadline.types.task_run_status

        out["task_run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["taskRunStatus"]
        )
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.step_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.step_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if data.get("taskRunStatusCounts") is not None:
        import capo_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            capo_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    if data.get("taskFailureRetryCount") is not None:
        out["task_failure_retry_count"] = data["taskFailureRetryCount"]
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
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
    if data.get("parameterSpace") is not None:
        import capo_deadline.types.parameter_space

        out["parameter_space"] = capo_deadline.types.parameter_space.deserialize_json(
            data["parameterSpace"]
        )
    return out
