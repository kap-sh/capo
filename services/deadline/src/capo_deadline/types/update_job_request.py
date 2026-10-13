"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
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


class UpdateJobRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the job to update.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the job to update.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID to update.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    target_task_run_status: NotRequired[
        "capo_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
    ]
    """<p>The task status to update the job's tasks to.</p>"""
    priority: NotRequired["capo_deadline.types.job_priority.JobPriority"]
    """<p>The updated job priority.</p>"""
    max_failed_tasks_count: NotRequired[
        "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """<p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>"""
    max_retries_per_task: NotRequired[
        "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """<p>The maximum number of retries for a job.</p>"""
    lifecycle_status: NotRequired[
        "capo_deadline.types.update_job_lifecycle_status.UpdateJobLifecycleStatus"
    ]
    """<p>The status of a job in its lifecycle. When you change the status of the job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived jobs and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>"""
    max_worker_count: NotRequired["capo_deadline.types.max_worker_count.MaxWorkerCount"]
    """<p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, the default is -1.</p> <p>The maximum number of workers that can process tasks in the job.</p>"""
    name: NotRequired["capo_deadline.types.job_name.JobName"]
    """<p>The updated job name.</p>"""
    description: NotRequired[
        "capo_deadline.types.job_description_override.JobDescriptionOverride"
    ]
    """<p>The updated job description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJobRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: UpdateJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
