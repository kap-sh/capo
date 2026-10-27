"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.attachments
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.ended_at
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_description
    import capo_deadline.types.job_id
    import capo_deadline.types.job_lifecycle_status
    import capo_deadline.types.job_name
    import capo_deadline.types.job_parameters
    import capo_deadline.types.job_priority
    import capo_deadline.types.job_target_task_run_status
    import capo_deadline.types.max_failed_tasks_count
    import capo_deadline.types.max_retries_per_task
    import capo_deadline.types.max_worker_count
    import capo_deadline.types.queue_id
    import capo_deadline.types.started_at
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.string
    import capo_deadline.types.task_failure_retry_count
    import capo_deadline.types.task_run_status
    import capo_deadline.types.task_run_status_counts
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class BatchGetJobItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the job."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the job."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    name: "capo_deadline.types.job_name.JobName"
    """The name of the job."""
    lifecycle_status: "capo_deadline.types.job_lifecycle_status.JobLifecycleStatus"
    """The life cycle status of the job."""
    lifecycle_status_message: "capo_deadline.types.string.String"
    """A message that communicates the status of the life cycle."""
    priority: "capo_deadline.types.job_priority.JobPriority"
    """The job priority."""
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
    task_run_status: NotRequired["capo_deadline.types.task_run_status.TaskRunStatus"]
    """The task run status for the job."""
    target_task_run_status: NotRequired[
        "capo_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """The task status to start with on the job."""
    task_run_status_counts: NotRequired[
        "capo_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    ]
    """The number of tasks for each run status for the job."""
    task_failure_retry_count: NotRequired[
        "capo_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """The number of times that tasks failed and were retried."""
    storage_profile_id: NotRequired[
        "capo_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """The storage profile ID associated with the job."""
    max_failed_tasks_count: NotRequired[
        "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """The number of task failures before the job stops running and is marked as <code>FAILED</code>."""
    max_retries_per_task: NotRequired[
        "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """The maximum number of retries per failed tasks."""
    parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """The parameters for the job."""
    attachments: NotRequired["capo_deadline.types.attachments.Attachments"]
    """The attachments for the job."""
    description: NotRequired["capo_deadline.types.job_description.JobDescription"]
    """The description of the job."""
    max_worker_count: NotRequired["capo_deadline.types.max_worker_count.MaxWorkerCount"]
    """The maximum number of worker hosts that can concurrently process a job."""
    source_job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """The job ID for the source job."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    out["name"] = value["name"]
    import capo_deadline.types.job_lifecycle_status

    out["lifecycleStatus"] = capo_deadline.types.job_lifecycle_status.serialize_json(
        value["lifecycle_status"]
    )
    out["lifecycleStatusMessage"] = value["lifecycle_status_message"]
    out["priority"] = value["priority"]
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
    if "task_run_status" in value:
        import capo_deadline.types.task_run_status

        out["taskRunStatus"] = capo_deadline.types.task_run_status.serialize_json(
            value["task_run_status"]
        )
    if "target_task_run_status" in value:
        import capo_deadline.types.job_target_task_run_status

        out["targetTaskRunStatus"] = (
            capo_deadline.types.job_target_task_run_status.serialize_json(
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
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "parameters" in value:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.serialize_json(
            value["parameters"]
        )
    if "attachments" in value:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.serialize_json(
            value["attachments"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "source_job_id" in value:
        out["sourceJobId"] = value["source_job_id"]
    return out


def deserialize_json(data: dict) -> BatchGetJobItem:
    out: BatchGetJobItem = {}  # type: ignore[typeddict-item]
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
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.job_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.job_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        import typing

        out["lifecycle_status"] = typing.cast(
            "capo_deadline.types.job_lifecycle_status.JobLifecycleStatus", ""
        )
    if data.get("lifecycleStatusMessage") is not None:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    else:
        out["lifecycle_status_message"] = ""
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
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
    if data.get("taskRunStatus") is not None:
        import capo_deadline.types.task_run_status

        out["task_run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["taskRunStatus"]
        )
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.job_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.job_target_task_run_status.deserialize_json(
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
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    if data.get("maxFailedTasksCount") is not None:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if data.get("maxRetriesPerTask") is not None:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if data.get("parameters") is not None:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("attachments") is not None:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.deserialize_json(
            data["attachments"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    if data.get("sourceJobId") is not None:
        out["source_job_id"] = data["sourceJobId"]
    return out


def redact_sensitive(value: BatchGetJobItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "attachments" in value:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.redact_sensitive(
            value["attachments"]
        )
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
