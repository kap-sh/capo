"""Generated from Smithy shape ``com.amazonaws.datazone#CreateNotebookInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.metadata
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_type
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id


class CreateNotebookInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.</p>"""
    owning_project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook.</p>"""
    name: "capo_datazone.types.notebook_name.NotebookName"
    """<p>The name of the notebook. The name must be between 1 and 256 characters.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the notebook.</p>"""
    type: NotRequired["capo_datazone.types.notebook_type.NotebookType"]
    """<p>The type of the notebook.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata.Metadata"]
    """<p>The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    parameters: NotRequired["capo_datazone.types.parameters.Parameters"]
    """<p>The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotebookInput) -> dict:
    out: dict = {}
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.serialize_json(value["type"])
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.serialize_json(value["metadata"])
    if "parameters" in value:
        import capo_datazone.types.parameters

        out["parameters"] = capo_datazone.types.parameters.serialize_json(
            value["parameters"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateNotebookInput:
    out: CreateNotebookInput = {}  # type: ignore[typeddict-item]
    if data.get("owningProjectIdentifier") is not None:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateNotebookInput.owning_project_identifier required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateNotebookInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_datazone.types.notebook_type

        out["type"] = capo_datazone.types.notebook_type.deserialize_json(data["type"])
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateNotebookInput) -> dict[str, Any]:
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
    return out
