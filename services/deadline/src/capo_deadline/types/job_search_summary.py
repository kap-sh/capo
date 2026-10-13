"""Generated from Smithy shape ``com.amazonaws.deadline#JobSearchSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.ended_at
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
    import capo_deadline.types.string
    import capo_deadline.types.task_failure_retry_count
    import capo_deadline.types.task_run_status
    import capo_deadline.types.task_run_status_counts
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class JobSearchSummary(TypedDict, closed=True):
    job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """<p>The job ID.</p>"""
    queue_id: NotRequired["capo_deadline.types.queue_id.QueueId"]
    """<p>The queue ID.</p>"""
    name: NotRequired["capo_deadline.types.job_name.JobName"]
    """<p>The job name.</p>"""
    lifecycle_status: NotRequired[
        "capo_deadline.types.job_lifecycle_status.JobLifecycleStatus"
    ]
    """<p>The life cycle status.</p>"""
    lifecycle_status_message: NotRequired["capo_deadline.types.string.String"]
    """<p>The life cycle status message.</p>"""
    task_run_status: NotRequired["capo_deadline.types.task_run_status.TaskRunStatus"]
    """<p>The task run status for the job.</p> <ul> <li> <p> <code>PENDING</code>–pending and waiting for resources.</p> </li> <li> <p> <code>READY</code>–ready to be processed.</p> </li> <li> <p> <code>ASSIGNED</code>–assigned and will run next on a worker.</p> </li> <li> <p> <code>SCHEDULED</code>–scheduled to be run on a worker.</p> </li> <li> <p> <code>INTERRUPTING</code>–being interrupted.</p> </li> <li> <p> <code>RUNNING</code>–running on a worker.</p> </li> <li> <p> <code>SUSPENDED</code>–the task is suspended.</p> </li> <li> <p> <code>CANCELED</code>–the task has been canceled.</p> </li> <li> <p> <code>FAILED</code>–the task has failed.</p> </li> <li> <p> <code>SUCCEEDED</code>–the task has succeeded.</p> </li> </ul>"""
    target_task_run_status: NotRequired[
        "capo_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """<p>The task status to update the job's tasks to.</p>"""
    task_run_status_counts: NotRequired[
        "capo_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    ]
    """<p>The number of tasks running on the job.</p>"""
    task_failure_retry_count: NotRequired[
        "capo_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The total number of times tasks from the job failed and were retried.</p>"""
    priority: NotRequired["capo_deadline.types.job_priority.JobPriority"]
    """<p>The job priority.</p>"""
    max_failed_tasks_count: NotRequired[
        "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """<p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>"""
    max_retries_per_task: NotRequired[
        "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """<p>The maximum number of retries for a job.</p>"""
    created_by: NotRequired["capo_deadline.types.created_by.CreatedBy"]
    """<p>The user or system that created this resource.</p>"""
    created_at: NotRequired["capo_deadline.types.created_at.CreatedAt"]
    """<p>The date and time the resource was created.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    job_parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """<p>The job parameters.</p>"""
    max_worker_count: NotRequired["capo_deadline.types.max_worker_count.MaxWorkerCount"]
    """<p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, the default is -1.</p>"""
    source_job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """<p>The job ID for the source job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobSearchSummary) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "queue_id" in value:
        out["queueId"] = value["queue_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "lifecycle_status" in value:
        import capo_deadline.types.job_lifecycle_status

        out["lifecycleStatus"] = (
            capo_deadline.types.job_lifecycle_status.serialize_json(
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
    if "priority" in value:
        out["priority"] = value["priority"]
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_deadline.types.created_at

        out["createdAt"] = capo_deadline.types.created_at.serialize_json(
            value["created_at"]
        )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "started_at" in value:
        import capo_deadline.types.started_at

        out["startedAt"] = capo_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "job_parameters" in value:
        import capo_deadline.types.job_parameters

        out["jobParameters"] = capo_deadline.types.job_parameters.serialize_json(
            value["job_parameters"]
        )
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "source_job_id" in value:
        out["sourceJobId"] = value["source_job_id"]
    return out


def deserialize_json(data: dict) -> JobSearchSummary:
    out: JobSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.job_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.job_lifecycle_status.deserialize_json(
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
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("maxFailedTasksCount") is not None:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if data.get("maxRetriesPerTask") is not None:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("jobParameters") is not None:
        import capo_deadline.types.job_parameters

        out["job_parameters"] = capo_deadline.types.job_parameters.deserialize_json(
            data["jobParameters"]
        )
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    if data.get("sourceJobId") is not None:
        out["source_job_id"] = data["sourceJobId"]
    return out


def redact_sensitive(value: JobSearchSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_parameters" in value:
        out["job_parameters"] = "*** Sensitive Data Redacted ***"
    return out
