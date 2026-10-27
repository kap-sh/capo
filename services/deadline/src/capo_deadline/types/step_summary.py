"""Generated from Smithy shape ``com.amazonaws.deadline#StepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.dependency_counts
    import capo_deadline.types.ended_at
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


class StepSummary(TypedDict, closed=True):
    step_id: "capo_deadline.types.step_id.StepId"
    """The step ID."""
    name: "capo_deadline.types.step_name.StepName"
    """The name of the step."""
    lifecycle_status: "capo_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    """The life cycle status."""
    lifecycle_status_message: NotRequired["capo_deadline.types.string.String"]
    """A message that describes the lifecycle of the step."""
    task_run_status: "capo_deadline.types.task_run_status.TaskRunStatus"
    """<p>The task run status for the job.</p> <ul> <li> <p> <code>PENDING</code>–pending and waiting for resources.</p> </li> <li> <p> <code>READY</code>–ready to process.</p> </li> <li> <p> <code>ASSIGNED</code>–assigned and will run next on a worker.</p> </li> <li> <p> <code>SCHEDULED</code>–scheduled to run on a worker.</p> </li> <li> <p> <code>INTERRUPTING</code>–being interrupted.</p> </li> <li> <p> <code>RUNNING</code>–running on a worker.</p> </li> <li> <p> <code>SUSPENDED</code>–the task is suspended.</p> </li> <li> <p> <code>CANCELED</code>–the task has been canceled.</p> </li> <li> <p> <code>FAILED</code>–the task has failed.</p> </li> <li> <p> <code>SUCCEEDED</code>–the task has succeeded.</p> </li> </ul>"""
    task_run_status_counts: (
        "capo_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    )
    """The number of tasks running on the job."""
    task_failure_retry_count: NotRequired[
        "capo_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """The total number of times tasks from the step failed and were retried."""
    target_task_run_status: NotRequired[
        "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """The task status to update the job's tasks to."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The date and time the resource was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user or system that created this resource."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """The date and time the resource started running."""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """The date and time the resource ended running."""
    dependency_counts: NotRequired[
        "capo_deadline.types.dependency_counts.DependencyCounts"
    ]
    """The number of dependencies for the step."""


# --- restJson1 ser/de ---
def serialize_json(value: StepSummary) -> dict:
    out: dict = {}
    out["stepId"] = value["step_id"]
    out["name"] = value["name"]
    import capo_deadline.types.step_lifecycle_status

    out["lifecycleStatus"] = capo_deadline.types.step_lifecycle_status.serialize_json(
        value["lifecycle_status"]
    )
    if "lifecycle_status_message" in value:
        out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    import capo_deadline.types.task_run_status

    out["taskRunStatus"] = capo_deadline.types.task_run_status.serialize_json(
        value["task_run_status"]
    )
    import capo_deadline.types.task_run_status_counts

    out["taskRunStatusCounts"] = (
        capo_deadline.types.task_run_status_counts.serialize_json(
            value["task_run_status_counts"]
        )
    )
    if "task_failure_retry_count" in value:
        out["taskFailureRetryCount"] = value["task_failure_retry_count"]
    if "target_task_run_status" in value:
        import capo_deadline.types.step_target_task_run_status

        out["targetTaskRunStatus"] = (
            capo_deadline.types.step_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "started_at" in value:
        import capo_deadline.types.started_at

        out["startedAt"] = capo_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "dependency_counts" in value:
        import capo_deadline.types.dependency_counts

        out["dependencyCounts"] = capo_deadline.types.dependency_counts.serialize_json(
            value["dependency_counts"]
        )
    return out


def deserialize_json(data: dict) -> StepSummary:
    out: StepSummary = {}  # type: ignore[typeddict-item]
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        out["step_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        import typing

        out["lifecycle_status"] = typing.cast(
            "capo_deadline.types.step_lifecycle_status.StepLifecycleStatus", ""
        )
    if data.get("lifecycleStatusMessage") is not None:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    if data.get("taskRunStatus") is not None:
        import capo_deadline.types.task_run_status

        out["task_run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["taskRunStatus"]
        )
    else:
        import typing

        out["task_run_status"] = typing.cast(
            "capo_deadline.types.task_run_status.TaskRunStatus", ""
        )
    if data.get("taskRunStatusCounts") is not None:
        import capo_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            capo_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    else:
        out["task_run_status_counts"] = {}
    if data.get("taskFailureRetryCount") is not None:
        out["task_failure_retry_count"] = data["taskFailureRetryCount"]
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.step_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.step_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
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
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("dependencyCounts") is not None:
        import capo_deadline.types.dependency_counts

        out["dependency_counts"] = (
            capo_deadline.types.dependency_counts.deserialize_json(
                data["dependencyCounts"]
            )
        )
    return out
