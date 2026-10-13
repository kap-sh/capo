"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateNotebookInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.cell_order
    import capo_datazone.types.client_token
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_config
    import capo_datazone.types.metadata
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_status
    import capo_datazone.types.notebook_type
    import capo_datazone.types.parameters


class UpdateNotebookInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>"""
    identifier: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to update.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The updated description of the notebook.</p>"""
    status: NotRequired["capo_datazone.types.notebook_status.NotebookStatus"]
    """<p>The updated status of the notebook.</p>"""
    name: NotRequired["capo_datazone.types.notebook_name.NotebookName"]
    """<p>The updated name of the notebook.</p>"""
    cell_order: NotRequired["capo_datazone.types.cell_order.CellOrder"]
    """<p>The updated ordered list of cells in the notebook.</p>"""
    type: NotRequired["capo_datazone.types.notebook_type.NotebookType"]
    """<p>The updated type of the notebook.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata.Metadata"]
    """<p>The updated metadata for the notebook, specified as key-value pairs.</p>"""
    parameters: NotRequired["capo_datazone.types.parameters.Parameters"]
    """<p>The updated sensitive parameters for the notebook, specified as key-value pairs.</p>"""
    environment_configuration: NotRequired[
        "capo_datazone.types.environment_config.EnvironmentConfig"
    ]
    """<p>The updated environment configuration for the notebook.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotebookInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.serialize_json(
            value["status"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "cell_order" in value:
        import capo_datazone.types.cell_order

        out["cellOrder"] = capo_datazone.types.cell_order.serialize_json(
            value["cell_order"]
        )
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
    if "environment_configuration" in value:
        import capo_datazone.types.environment_config

        out["environmentConfiguration"] = (
            capo_datazone.types.environment_config.serialize_json(
                value["environment_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateNotebookInput:
    out: UpdateNotebookInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.notebook_status

        out["status"] = capo_datazone.types.notebook_status.deserialize_json(
            data["status"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("cellOrder") is not None:
        import capo_datazone.types.cell_order

        out["cell_order"] = capo_datazone.types.cell_order.deserialize_json(
            data["cellOrder"]
        )
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
    if data.get("environmentConfiguration") is not None:
        import capo_datazone.types.environment_config

        out["environment_configuration"] = (
            capo_datazone.types.environment_config.deserialize_json(
                data["environmentConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateNotebookInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        import capo_datazone.types.metadata

        out["metadata"] = capo_datazone.types.metadata.redact_sensitive(
            value["metadata"]
        )
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
