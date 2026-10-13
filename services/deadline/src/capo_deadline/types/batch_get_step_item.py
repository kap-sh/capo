"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.dependency_counts
    import capo_deadline.types.ended_at
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.parameter_space
    import capo_deadline.types.queue_id
    import capo_deadline.types.started_at
    import capo_deadline.types.step_description
    import capo_deadline.types.step_id
    import capo_deadline.types.step_lifecycle_status
    import capo_deadline.types.step_name
    import capo_deadline.types.step_required_capabilities
    import capo_deadline.types.step_target_task_run_status
    import capo_deadline.types.string
    import capo_deadline.types.task_failure_retry_count
    import capo_deadline.types.task_run_status
    import capo_deadline.types.task_run_status_counts
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class BatchGetStepItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the step.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the step.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID of the step.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID.</p>"""
    name: "capo_deadline.types.step_name.StepName"
    """<p>The name of the step.</p>"""
    lifecycle_status: "capo_deadline.types.step_lifecycle_status.StepLifecycleStatus"
    """<p>The life cycle status of the step.</p>"""
    lifecycle_status_message: NotRequired["capo_deadline.types.string.String"]
    """<p>A message that communicates the status of the life cycle.</p>"""
    task_run_status: "capo_deadline.types.task_run_status.TaskRunStatus"
    """<p>The task run status for the step.</p>"""
    task_run_status_counts: (
        "capo_deadline.types.task_run_status_counts.TaskRunStatusCounts"
    )
    """<p>The number of tasks for each run status for the step.</p>"""
    task_failure_retry_count: NotRequired[
        "capo_deadline.types.task_failure_retry_count.TaskFailureRetryCount"
    ]
    """<p>The number of times that tasks failed and were retried.</p>"""
    target_task_run_status: NotRequired[
        "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus"
    ]
    """<p>The task status to start with on the step.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    started_at: NotRequired["capo_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    dependency_counts: NotRequired[
        "capo_deadline.types.dependency_counts.DependencyCounts"
    ]
    """<p>The number of dependencies for the step.</p>"""
    required_capabilities: NotRequired[
        "capo_deadline.types.step_required_capabilities.StepRequiredCapabilities"
    ]
    """<p>The required capabilities for the step.</p>"""
    parameter_space: NotRequired["capo_deadline.types.parameter_space.ParameterSpace"]
    """<p>The parameter space for the step.</p>"""
    description: NotRequired["capo_deadline.types.step_description.StepDescription"]
    """<p>The description of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
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
    if "required_capabilities" in value:
        import capo_deadline.types.step_required_capabilities

        out["requiredCapabilities"] = (
            capo_deadline.types.step_required_capabilities.serialize_json(
                value["required_capabilities"]
            )
        )
    if "parameter_space" in value:
        import capo_deadline.types.parameter_space

        out["parameterSpace"] = capo_deadline.types.parameter_space.serialize_json(
            value["parameter_space"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BatchGetStepItem:
    out: BatchGetStepItem = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetStepItem.farm_id required")
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("BatchGetStepItem.queue_id required")
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("BatchGetStepItem.job_id required")
    if data.get("stepId") is not None:
        out["step_id"] = data["stepId"]
    else:
        raise DeserializationError("BatchGetStepItem.step_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchGetStepItem.name required")
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.step_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.step_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        raise DeserializationError("BatchGetStepItem.lifecycle_status required")
    if data.get("lifecycleStatusMessage") is not None:
        out["lifecycle_status_message"] = data["lifecycleStatusMessage"]
    if data.get("taskRunStatus") is not None:
        import capo_deadline.types.task_run_status

        out["task_run_status"] = capo_deadline.types.task_run_status.deserialize_json(
            data["taskRunStatus"]
        )
    else:
        raise DeserializationError("BatchGetStepItem.task_run_status required")
    if data.get("taskRunStatusCounts") is not None:
        import capo_deadline.types.task_run_status_counts

        out["task_run_status_counts"] = (
            capo_deadline.types.task_run_status_counts.deserialize_json(
                data["taskRunStatusCounts"]
            )
        )
    else:
        raise DeserializationError("BatchGetStepItem.task_run_status_counts required")
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
        raise DeserializationError("BatchGetStepItem.created_at required")
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("BatchGetStepItem.created_by required")
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
    if data.get("requiredCapabilities") is not None:
        import capo_deadline.types.step_required_capabilities

        out["required_capabilities"] = (
            capo_deadline.types.step_required_capabilities.deserialize_json(
                data["requiredCapabilities"]
            )
        )
    if data.get("parameterSpace") is not None:
        import capo_deadline.types.parameter_space

        out["parameter_space"] = capo_deadline.types.parameter_space.deserialize_json(
            data["parameterSpace"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: BatchGetStepItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
