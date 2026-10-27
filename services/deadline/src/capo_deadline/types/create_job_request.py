"""Generated from Smithy shape ``com.amazonaws.deadline#CreateJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.attachments
    import capo_deadline.types.client_token
    import capo_deadline.types.create_job_target_task_run_status
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_description_override
    import capo_deadline.types.job_id
    import capo_deadline.types.job_name
    import capo_deadline.types.job_parameters
    import capo_deadline.types.job_priority
    import capo_deadline.types.job_template
    import capo_deadline.types.job_template_type
    import capo_deadline.types.max_failed_tasks_count
    import capo_deadline.types.max_retries_per_task
    import capo_deadline.types.max_worker_count
    import capo_deadline.types.queue_id
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.tags


class CreateJobRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to connect to the job."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The ID of the queue that the job is submitted to."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    template: NotRequired["capo_deadline.types.job_template.JobTemplate"]
    """The job template to use for this job."""
    template_type: NotRequired["capo_deadline.types.job_template_type.JobTemplateType"]
    """The file type for the job template."""
    priority: "capo_deadline.types.job_priority.JobPriority"
    """The priority of the job. The highest priority (first scheduled) is 100. When two jobs have the same priority, the oldest job is scheduled first."""
    parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """The parameters for the job."""
    attachments: NotRequired["capo_deadline.types.attachments.Attachments"]
    """The attachments for the job. Attach files required for the job to run to a render job."""
    storage_profile_id: NotRequired[
        "capo_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """The storage profile ID for the storage profile to connect to the job."""
    target_task_run_status: NotRequired[
        "capo_deadline.types.create_job_target_task_run_status.CreateJobTargetTaskRunStatus"
    ]
    """The initial job status when it is created. Jobs that are created with a <code>SUSPENDED</code> status will not run until manually requeued."""
    max_failed_tasks_count: NotRequired[
        "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
    ]
    """The number of task failures before the job stops running and is marked as <code>FAILED</code>."""
    max_retries_per_task: NotRequired[
        "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
    ]
    """The maximum number of retries for each task."""
    max_worker_count: NotRequired["capo_deadline.types.max_worker_count.MaxWorkerCount"]
    """The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers. You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers. If you don't specify the <code>maxWorkerCount</code>, Deadline Cloud won't throttle the number of workers used to process the job."""
    source_job_id: NotRequired["capo_deadline.types.job_id.JobId"]
    """The job ID for the source job."""
    name_override: NotRequired["capo_deadline.types.job_name.JobName"]
    """A custom name to override the job name derived from the job template."""
    description_override: NotRequired[
        "capo_deadline.types.job_description_override.JobDescriptionOverride"
    ]
    """A custom description to override the job description derived from the job template."""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """The tags to add to your job. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    if "template" in value:
        out["template"] = value["template"]
    if "template_type" in value:
        import capo_deadline.types.job_template_type

        out["templateType"] = capo_deadline.types.job_template_type.serialize_json(
            value["template_type"]
        )
    out["priority"] = value["priority"]
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
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "target_task_run_status" in value:
        import capo_deadline.types.create_job_target_task_run_status

        out["targetTaskRunStatus"] = (
            capo_deadline.types.create_job_target_task_run_status.serialize_json(
                value["target_task_run_status"]
            )
        )
    if "max_failed_tasks_count" in value:
        out["maxFailedTasksCount"] = value["max_failed_tasks_count"]
    if "max_retries_per_task" in value:
        out["maxRetriesPerTask"] = value["max_retries_per_task"]
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "source_job_id" in value:
        out["sourceJobId"] = value["source_job_id"]
    if "name_override" in value:
        out["nameOverride"] = value["name_override"]
    if "description_override" in value:
        out["descriptionOverride"] = value["description_override"]
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("template") is not None:
        out["template"] = data["template"]
    if data.get("templateType") is not None:
        import capo_deadline.types.job_template_type

        out["template_type"] = capo_deadline.types.job_template_type.deserialize_json(
            data["templateType"]
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
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
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    if data.get("targetTaskRunStatus") is not None:
        import capo_deadline.types.create_job_target_task_run_status

        out["target_task_run_status"] = (
            capo_deadline.types.create_job_target_task_run_status.deserialize_json(
                data["targetTaskRunStatus"]
            )
        )
    if data.get("maxFailedTasksCount") is not None:
        out["max_failed_tasks_count"] = data["maxFailedTasksCount"]
    if data.get("maxRetriesPerTask") is not None:
        out["max_retries_per_task"] = data["maxRetriesPerTask"]
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    if data.get("sourceJobId") is not None:
        out["source_job_id"] = data["sourceJobId"]
    if data.get("nameOverride") is not None:
        out["name_override"] = data["nameOverride"]
    if data.get("descriptionOverride") is not None:
        out["description_override"] = data["descriptionOverride"]
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "attachments" in value:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.redact_sensitive(
            value["attachments"]
        )
    if "description_override" in value:
        out["description_override"] = "*** Sensitive Data Redacted ***"
    return out
