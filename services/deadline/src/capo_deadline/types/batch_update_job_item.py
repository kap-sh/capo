"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_description_override
    import capo_deadline.types.job_id
    import capo_deadline.types.job_name
    import capo_deadline.types.job_priority
    import capo_deadline.types.job_target_task_run_status
    import capo_deadline.types.max_failed_tasks_count
    import capo_deadline.types.max_retries_per_task
    import capo_deadline.types.max_worker_count
    import capo_deadline.types.queue_id
    import capo_deadline.types.update_job_lifecycle_status


class BatchUpdateJobItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the job to update."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the job to update."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID of the job to update."""
    target_task_run_status: NotRequired[
        "capo_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """The task status to update the job's tasks to."""
    priority: NotRequired["capo_deadline.types.job_priority.JobPriority"]
    """The job priority to update."""
    max_failed_tasks_count: NotRequired[
        "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """The number of task failures before the job stops running and is marked as <code>FAILED</code>."""
    max_retries_per_task: NotRequired[
        "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """The maximum number of retries per failed tasks."""
    lifecycle_status: NotRequired[
        "capo_deadline.types.update_job_lifecycle_status.UpdateJobLifecycleStatus"
    ]
    """<p>The status of a job in its lifecycle. When you change the status of the job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived job and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>"""
    max_worker_count: NotRequired["capo_deadline.types.max_worker_count.MaxWorkerCount"]
    """The maximum number of worker hosts that can concurrently process a job."""
    name: NotRequired["capo_deadline.types.job_name.JobName"]
    """The name of the job to update."""
    description: NotRequired[
        "capo_deadline.types.job_description_override.JobDescriptionOverride"
    ]
    """The description of the job to update."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    if "target_task_run_status" in value:
        import capo_deadline.types.job_target_task_run_status

        out["targetTaskRunStatus"] = (
            capo_deadline.types.job_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "lifecycle_status" in value:
        import capo_deadline.types.update_job_lifecycle_status

        out["lifecycleStatus"] = (
            capo_deadline.types.update_job_lifecycle_status.serialize_json(
                value["lifecycle_status"]
            )
        )
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BatchUpdateJobItem:
    out: BatchUpdateJobItem = {}  # type: ignore[typeddict-item]
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
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.job_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.job_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("maxFailedTasksCount") is not None:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if data.get("maxRetriesPerTask") is not None:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.update_job_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.update_job_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: BatchUpdateJobItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
