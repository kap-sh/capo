"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateNotebookOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.cell_order
    import capo_datazone.types.compute_id
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_config
    import capo_datazone.types.git_metadata
    import capo_datazone.types.metadata
    import capo_datazone.types.notebook_error
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_status
    import capo_datazone.types.notebook_type
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class UpdateNotebookOutput(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    name: "capo_datazone.types.notebook_name.NotebookName"
    """<p>The name of the notebook.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    cell_order: "capo_datazone.types.cell_order.CellOrder"
    """<p>The ordered list of cells in the notebook.</p>"""
    status: "capo_datazone.types.notebook_status.NotebookStatus"
    """<p>The status of the notebook.</p>"""
    type: NotRequired["capo_datazone.types.notebook_type.NotebookType"]
    """<p>The type of the notebook.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook was last updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook.</p>"""
    locked_by: NotRequired["str"]
    """<p>The identifier of the user who locked the notebook.</p>"""
    locked_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook was locked.</p>"""
    lock_expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook lock expires.</p>"""
    compute_id: NotRequired["capo_datazone.types.compute_id.ComputeId"]
    """<p>The identifier of the compute associated with the notebook.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata.Metadata"]
    """<p>The metadata of the notebook.</p>"""
    parameters: NotRequired["capo_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters of the notebook.</p>"""
    environment_configuration: NotRequired[
        "capo_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The environment configuration of the notebook.</p>"""
    error: NotRequired["capo_datazone.types.notebook_error.NotebookError"]
    """<p>The error details if the notebook is in a failed state.</p>"""
    git_metadata: NotRequired["capo_datazone.types.git_metadata.GitMetadata"]
    """<p>The Git metadata associated with the notebook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotebookOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["owningProjectId"] = value["owning_project_id"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.cell_order

    out["cellOrder"] = capo_datazone.types.cell_order.serialize_json(
        value["cell_order"]
    )
    import capo_datazone.types.notebook_status

    out["status"] = capo_datazone.types.notebook_status.serialize_json(value["status"])
    if "type" in value:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
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
    if "locked_by" in value:
        out["lockedBy"] = value["locked_by"]
    if "locked_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["lockedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["locked_at"]
        )
    if "lock_expires_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["lockExpiresAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["lock_expires_at"]
        )
    if "compute_id" in value:
        out["computeId"] = value["compute_id"]
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.serialize_json(value["metadata"])
    if "parameters" in value:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "environment_configuration" in value:
        import capo_datazone.types.environment_config

        out["environmentConfiguration"] = (
            capo_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "error" in value:
        import capo_datazone.types.notebook_error

        out["error"] = capo_datazone.types.notebook_error.serialize_json(value["error"])
    if "git_metadata" in value:
        import capo_datazone.types.git_metadata

        out["gitMetadata"] = capo_datazone.types.git_metadata.serialize_json(
            value["git_metadata"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNotebookOutput:
    out: UpdateNotebookOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateNotebookOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateNotebookOutput.name required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("UpdateNotebookOutput.owning_project_id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateNotebookOutput.domain_id required")
    if data.get("cellOrder") is not None:
        import capo_datazone.types.cell_order

        out["cell_order"] = capo_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
    else:
        raise DeserializationError("UpdateNotebookOutput.cell_order required")
    if data.get("status") is not None:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateNotebookOutput.status required")
    if data.get("type") is not None:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.deserialize_json(data["type"])
    if data.get("description") is not None:
        out["description"] = data["description"]
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
    if data.get("lockedBy") is not None:
        out["locked_by"] = data["lockedBy"]
    if data.get("lockedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["locked_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["lockedAt"]
        )
    if data.get("lockExpiresAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["lock_expires_at"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["lockExpiresAt"]
            )
        )
    if data.get("computeId") is not None:
        out["compute_id"] = data["computeId"]
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
    if data.get("environmentConfiguration") is not None:
        import capo_datazone.types.environment_config

        out["environment_configuration"] = (
            capo_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if data.get("error") is not None:
        import capo_datazone.types.notebook_error

        out["error"] = capo_datazone.types.notebook_error.deserialize_json(
            data["error"]
        )
    if data.get("gitMetadata") is not None:
        import capo_datazone.types.git_metadata

        out["git_metadata"] = capo_datazone.types.git_metadata.deserialize_json(
            data["gitMetadata"]
        )
    return out


def redact_sensitive(value: UpdateNotebookOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.redact_sensitive(
            value["metadata"]
        )
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "git_metadata" in value:
        import capo_datazone.types.git_metadata

        out["git_metadata"] = capo_datazone.types.git_metadata.redact_sensitive(
            value["git_metadata"]
        )
    return out
