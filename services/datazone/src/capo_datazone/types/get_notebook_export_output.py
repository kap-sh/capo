"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookExportOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.completed_at
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.export_id
    import capo_datazone.types.file_format
    import capo_datazone.types.notebook_export_error
    import capo_datazone.types.notebook_export_status
    import capo_datazone.types.notebook_id
    import capo_datazone.types.output_location
    import capo_datazone.types.project_id


class GetNotebookExportOutput(TypedDict, closed=True):
    id: "capo_datazone.types.export_id.ExportId"
    """<p>The identifier of the notebook export.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    notebook_id: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    file_format: "capo_datazone.types.file_format.FileFormat"
    """<p>The file format of the notebook export.</p>"""
    status: "capo_datazone.types.notebook_export_status.NotebookExportStatus"
    """<p>The status of the notebook export.</p>"""
    output_location: NotRequired["capo_datazone.types.output_location.OutputLocation"]
    """<p>The output location of the exported notebook in Amazon Simple Storage Service.</p>"""
    error: NotRequired["capo_datazone.types.notebook_export_error.NotebookExportError"]
    """<p>The error details if the notebook export failed.</p>"""
    completed_at: NotRequired["capo_datazone.types.completed_at.CompletedAt"]
    """<p>The timestamp of when the notebook export completed.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook export was started.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who started the notebook export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookExportOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    out["notebookId"] = value["notebook_id"]
    import capo_datazone.types.file_format

    out["fileFormat"] = capo_datazone.types.file_format.serialize_json(
        value["file_format"]
    )
    import capo_datazone.types.notebook_export_status

    out["status"] = capo_datazone.types.notebook_export_status.serialize_json(
        value["status"]
    )
    if "output_location" in value:
        import capo_datazone.types.output_location

        out["outputLocation"] = capo_datazone.types.output_location.serialize_json(
            value["output_location"]
        )
    if "error" in value:
        import capo_datazone.types.notebook_export_error

        out["error"] = capo_datazone.types.notebook_export_error.serialize_json(
            value["error"]
        )
    if "completed_at" in value:
        import capo_datazone.types.completed_at

        out["completedAt"] = capo_datazone.types.completed_at.serialize_json(
            value["completed_at"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> GetNotebookExportOutput:
    out: GetNotebookExportOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetNotebookExportOutput.id required")
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.domain_id required")
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.owning_project_id required")
    if data.get("notebookId") is not None:
        out["notebook_id"] = data["notebookId"]
    else:
        raise DeserializationError("GetNotebookExportOutput.notebook_id required")
    if data.get("fileFormat") is not None:
        import capo_datazone.types.file_format

        out["file_format"] = capo_datazone.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("GetNotebookExportOutput.file_format required")
    if data.get("status") is not None:
        import capo_datazone.types.notebook_export_status

        out["status"] = capo_datazone.types.notebook_export_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetNotebookExportOutput.status required")
    if data.get("outputLocation") is not None:
        import capo_datazone.types.output_location

        out["output_location"] = capo_datazone.types.output_location.deserialize_json(
            data["outputLocation"]
        )
    if data.get("error") is not None:
        import capo_datazone.types.notebook_export_error

        out["error"] = capo_datazone.types.notebook_export_error.deserialize_json(
            data["error"]
        )
    if data.get("completedAt") is not None:
        import capo_datazone.types.completed_at

        out["completed_at"] = capo_datazone.types.completed_at.deserialize_json(
            data["completedAt"]
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out


def redact_sensitive(value: GetNotebookExportOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "output_location" in value:
        import capo_datazone.types.output_location

        out["output_location"] = capo_datazone.types.output_location.redact_sensitive(
            value["output_location"]
        )
    return out
