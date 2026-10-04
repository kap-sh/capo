"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.cell_order
    import capo_datazone.types.compute_config
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_config
    import capo_datazone.types.metadata
    import capo_datazone.types.network_config
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_run_error
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.notification_config
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id
    import capo_datazone.types.schedule_id
    import capo_datazone.types.storage_config
    import capo_datazone.types.timeout_config
    import capo_datazone.types.trigger_source
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetNotebookRunOutput(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    notebook_id: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    schedule_id: NotRequired["capo_datazone.types.schedule_id.ScheduleId"]
    """<p>The identifier of the schedule associated with the notebook run.</p>"""
    status: "capo_datazone.types.notebook_run_status.NotebookRunStatus"
    """<p>The status of the notebook run.</p>"""
    cell_order: NotRequired["capo_datazone.types.cell_order.CellOrder"]
    """<p>The ordered list of cells in the notebook run.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata.Metadata"]
    """<p>The metadata of the notebook run.</p>"""
    parameters: NotRequired["capo_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters of the notebook run.</p>"""
    compute_configuration: NotRequired[
        "capo_datazone.types.compute_config.ComputeConfig"
    ]
    """<p>The compute configuration of the notebook run.</p>"""
    network_configuration: NotRequired[
        "capo_datazone.types.network_config.NetworkConfig"
    ]
    """<p>The network configuration of the notebook run.</p>"""
    timeout_configuration: NotRequired[
        "capo_datazone.types.timeout_config.TimeoutConfig"
    ]
    """<p>The timeout configuration of the notebook run.</p>"""
    environment_configuration: NotRequired[
        "capo_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The environment configuration of the notebook run, including image version and package settings.</p>"""
    storage_configuration: NotRequired[
        "capo_datazone.types.storage_config.StorageConfig"
    ]
    """<p>The storage configuration of the notebook run, including the Amazon Simple Storage Service path and KMS key ARN.</p>"""
    notification_configuration: NotRequired[
        "capo_datazone.types.notification_config.NotificationConfig"
    ]
    """<p>The notification configuration of the notebook run, including the notebook run states that trigger notifications.</p>"""
    trigger_source: NotRequired["capo_datazone.types.trigger_source.TriggerSource"]
    """<p>The source that triggered the notebook run.</p>"""
    error: NotRequired["capo_datazone.types.notebook_run_error.NotebookRunError"]
    """<p>The error details if the notebook run failed.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook run was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook run.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook run was last updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook run.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run started executing.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookRunOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    out["notebookId"] = value["notebook_id"]
    if "schedule_id" in value:
        out["scheduleId"] = value["schedule_id"]
    import capo_datazone.types.notebook_run_status

    out["status"] = capo_datazone.types.notebook_run_status.serialize_json(
        value["status"]
    )
    if "cell_order" in value:
        import capo_datazone.types.cell_order

        out["cellOrder"] = capo_datazone.types.cell_order.serialize_json(
            value["cell_order"]
        )
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.serialize_json(value["metadata"])
    if "parameters" in value:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "compute_configuration" in value:
        import capo_datazone.types.compute_config

        out["computeConfiguration"] = capo_datazone.types.compute_config.serialize_json(
            value["compute_configuration"]
        )
    if "network_configuration" in value:
        import capo_datazone.types.network_config

        out["networkConfiguration"] = capo_datazone.types.network_config.serialize_json(
            value["network_configuration"]
        )
    if "timeout_configuration" in value:
        import capo_datazone.types.timeout_config

        out["timeoutConfiguration"] = capo_datazone.types.timeout_config.serialize_json(
            value["timeout_configuration"]
        )
    if "environment_configuration" in value:
        import capo_datazone.types.environment_config

        out["environmentConfiguration"] = (
            capo_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "storage_configuration" in value:
        import capo_datazone.types.storage_config

        out["storageConfiguration"] = capo_datazone.types.storage_config.serialize_json(
            value["storage_configuration"]
        )
    if "notification_configuration" in value:
        import capo_datazone.types.notification_config

        out["notificationConfiguration"] = (
            capo_datazone.types.notification_config.serialize_json(
                value["notification_configuration"]
            )
        )
    if "trigger_source" in value:
        import capo_datazone.types.trigger_source

        out["triggerSource"] = capo_datazone.types.trigger_source.serialize_json(
            value["trigger_source"]
        )
    if "error" in value:
        import capo_datazone.types.notebook_run_error

        out["error"] = capo_datazone.types.notebook_run_error.serialize_json(
            value["error"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "started_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["startedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["completedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> GetNotebookRunOutput:
    out: GetNotebookRunOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetNotebookRunOutput.id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetNotebookRunOutput.domain_id required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GetNotebookRunOutput.owning_project_id required")
    if data.get("notebookId") is not None:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("GetNotebookRunOutput.notebook_id required")
    if data.get("scheduleId") is not None:
        out["schedule_id"] = data["scheduleId"]
    if data.get("status") is not None:
        import capo_datazone.types.notebook_run_status

        out["status"] = capo_datazone.types.notebook_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetNotebookRunOutput.status required")
    if data.get("cellOrder") is not None:
        import capo_datazone.types.cell_order

        out["cell_order"] = capo_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
    if data.get("metadata") is not None:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("parameters") is not None:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("computeConfiguration") is not None:
        import capo_datazone.types.compute_config

        out["compute_configuration"] = (
            capo_datazone.types.compute_config.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if data.get("networkConfiguration") is not None:
        import capo_datazone.types.network_config

        out["network_configuration"] = (
            capo_datazone.types.network_config.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("timeoutConfiguration") is not None:
        import capo_datazone.types.timeout_config

        out["timeout_configuration"] = (
            capo_datazone.types.timeout_config.deserialize_json(
                data["timeoutConfiguration"]
            )
        )
    if data.get("environmentConfiguration") is not None:
        import capo_datazone.types.environment_config

        out["environment_configuration"] = (
            capo_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if data.get("storageConfiguration") is not None:
        import capo_datazone.types.storage_config

        out["storage_configuration"] = (
            capo_datazone.types.storage_config.deserialize_json(
                data["storageConfiguration"]
            )
        )
    if data.get("notificationConfiguration") is not None:
        import capo_datazone.types.notification_config

        out["notification_configuration"] = (
            capo_datazone.types.notification_config.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    if data.get("triggerSource") is not None:
        import capo_datazone.types.trigger_source

        out["trigger_source"] = capo_datazone.types.trigger_source.deserialize_json(
            data["triggerSource"]
        )
    if data.get("error") is not None:
        import capo_datazone.types.notebook_run_error

        out["error"] = capo_datazone.types.notebook_run_error.deserialize_json(
            data["error"]
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("startedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["started_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("completedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["completed_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["completedAt"]
        )
    return out
