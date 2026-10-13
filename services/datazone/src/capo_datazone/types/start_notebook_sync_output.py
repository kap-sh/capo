"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookSyncOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.git_metadata
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_status
    import capo_datazone.types.project_id
    import capo_datazone.types.source_location


class StartNotebookSyncOutput(TypedDict, closed=True):
    notebook_id: NotRequired["capo_datazone.types.notebook_id.NotebookId"]
    """<p>The identifier of the synced notebook.</p>"""
    status: NotRequired["capo_datazone.types.notebook_status.NotebookStatus"]
    """<p>The status of the notebook sync.</p>"""
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that owns the synced notebook.</p>"""
    source_location: NotRequired["capo_datazone.types.source_location.SourceLocation"]
    """<p>The source location from which the notebook was synced.</p>"""
    git_metadata: NotRequired["capo_datazone.types.git_metadata.GitMetadata"]
    """<p>The Git metadata associated with the synced notebook.</p>"""
    name: NotRequired["capo_datazone.types.notebook_name.NotebookName"]
    """<p>The name of the synced notebook.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the synced notebook.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook sync was started.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who started the notebook sync.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookSyncOutput) -> dict:
    out: dict = {}
    if "notebook_id" in value:
        out["notebookId"] = value["notebook_id"]
    if "status" in value:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.serialize_json(
            value["status"]
        )
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "source_location" in value:
        import capo_datazone.types.source_location

        out["sourceLocation"] = capo_datazone.types.source_location.serialize_json(
            value["source_location"]
        )
    if "git_metadata" in value:
        import capo_datazone.types.git_metadata

        out["gitMetadata"] = capo_datazone.types.git_metadata.serialize_json(
            value["git_metadata"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> StartNotebookSyncOutput:
    out: StartNotebookSyncOutput = {}  # type: ignore[typeddict-item]
    if data.get("notebookId") is not None:
        out["notebook_id"] = data["notebookId"]
    if data.get("status") is not None:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    if data.get("sourceLocation") is not None:
        import capo_datazone.types.source_location

        out["source_location"] = capo_datazone.types.source_location.deserialize_json(
            data["sourceLocation"]
        )
    if data.get("gitMetadata") is not None:
        import capo_datazone.types.git_metadata

        out["git_metadata"] = capo_datazone.types.git_metadata.deserialize_json(
            data["gitMetadata"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out


def redact_sensitive(value: StartNotebookSyncOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_location" in value:
        import capo_datazone.types.source_location

        out["source_location"] = capo_datazone.types.source_location.redact_sensitive(
            value["source_location"]
        )
    if "git_metadata" in value:
        import capo_datazone.types.git_metadata

        out["git_metadata"] = capo_datazone.types.git_metadata.redact_sensitive(
            value["git_metadata"]
        )
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
