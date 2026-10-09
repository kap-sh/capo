"""Generated from Smithy shape ``com.amazonaws.datazone#StartNotebookImportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_type
    import capo_datazone.types.project_id
    import capo_datazone.types.source_location


class StartNotebookImportInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to import the notebook.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that will own the imported notebook.</p>"""
    source_location: "capo_datazone.types.source_location.SourceLocation"
    """<p>The source location of the notebook to import. Specify either a single Amazon Simple Storage Service URI, or a list of objects to import as the notebook's cells.</p>"""
    name: "capo_datazone.types.notebook_name.NotebookName"
    """<p>The name of the imported notebook. The name must be between 1 and 256 characters.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the imported notebook.</p>"""
    type: NotRequired["capo_datazone.types.notebook_type.NotebookType"]
    """<p>The type of the notebook to import. If not specified, defaults to <code>DATA</code>.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNotebookImportInput) -> dict:
    out: dict = {}
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    import capo_datazone.types.source_location

    out["sourceLocation"] = capo_datazone.types.source_location.serialize_json(
        value["source_location"]
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.serialize_json(value["type"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartNotebookImportInput:
    out: StartNotebookImportInput = {}  # type: ignore[typeddict-item]
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "StartNotebookImportInput.owning_project_identifier required"
        )
    if data.get("sourceLocation") is not None:
        import capo_datazone.types.source_location

        out["source_location"] = capo_datazone.types.source_location.deserialize_json(
            data["sourceLocation"]
        )
    else:
        raise DeserializationError("StartNotebookImportInput.source_location required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartNotebookImportInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.deserialize_json(data["type"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
