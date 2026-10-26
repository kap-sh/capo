"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookSyncInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.git_metadata
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.project_id
    import capo_datazone.types.source_location


class StartNotebookSyncInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to sync the notebook.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that will own the synced notebook.</p>"""
    source_location: "capo_datazone.types.source_location.SourceLocation"
    """<p>The source location of the notebook to sync. This specifies the Amazon Simple Storage Service URI of the notebook file.</p>"""
    git_metadata: NotRequired["capo_datazone.types.git_metadata.GitMetadata"]
    """<p>The Git metadata for the notebook sync, including repository, branch, and commit information.</p>"""
    notebook_id: NotRequired["capo_datazone.types.notebook_id.NotebookId"]
    """<p>The identifier of an existing notebook to sync. If not specified, a new notebook is created.</p>"""
    name: NotRequired["capo_datazone.types.notebook_name.NotebookName"]
    """<p>The name of the notebook. The name must be between 1 and 256 characters.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookSyncInput) -> dict:
    out: dict = {}
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    import capo_datazone.types.source_location

    out["sourceLocation"] = capo_datazone.types.source_location.serialize_json(
        value["source_location"]
    )
    if "git_metadata" in value:
        import capo_datazone.types.git_metadata

        out["gitMetadata"] = capo_datazone.types.git_metadata.serialize_json(
            value["git_metadata"]
        )
    if "notebook_id" in value:
        out["notebookId"] = value["notebook_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartNotebookSyncInput:
    out: StartNotebookSyncInput = {}  # type: ignore[typeddict-item]
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        out["owning_project_identifier"] = ""
    if data.get("sourceLocation") is not None:
        import capo_datazone.types.source_location

        out["source_location"] = capo_datazone.types.source_location.deserialize_json(
            data["sourceLocation"]
        )
    else:
        out["source_location"] = {"$unknown": {"name": ""}}
    if data.get("gitMetadata") is not None:
        import capo_datazone.types.git_metadata

        out["git_metadata"] = capo_datazone.types.git_metadata.deserialize_json(
            data["gitMetadata"]
        )
    if data.get("notebookId") is not None:
        out["notebook_id"] = data["notebookId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: StartNotebookSyncInput) -> dict[str, Any]:
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
