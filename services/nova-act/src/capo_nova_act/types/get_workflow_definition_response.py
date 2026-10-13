"""Generated from Smithy shape ``com.amazonaws.novaact#GetWorkflowDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.date_timestamp
    import capo_nova_act.types.workflow_definition_arn
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_definition_status
    import capo_nova_act.types.workflow_description
    import capo_nova_act.types.workflow_export_config


class GetWorkflowDefinitionResponse(TypedDict, closed=True):
    name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    """<p>The name of the workflow definition.</p>"""
    arn: "capo_nova_act.types.workflow_definition_arn.WorkflowDefinitionArn"
    """<p>The Amazon Resource Name (ARN) of the workflow definition.</p>"""
    created_at: "capo_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the workflow definition was created.</p>"""
    description: NotRequired[
        "capo_nova_act.types.workflow_description.WorkflowDescription"
    ]
    """<p>The description of the workflow definition.</p>"""
    export_config: NotRequired[
        "capo_nova_act.types.workflow_export_config.WorkflowExportConfig"
    ]
    """<p>The export configuration for the workflow definition.</p>"""
    status: "capo_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The current status of the workflow definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowDefinitionResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_nova_act.types.date_timestamp

    out["createdAt"] = capo_nova_act.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "export_config" in value:
        import capo_nova_act.types.workflow_export_config

        out["exportConfig"] = capo_nova_act.types.workflow_export_config.serialize_json(
            value["export_config"]
        )
    import capo_nova_act.types.workflow_definition_status

    out["status"] = capo_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GetWorkflowDefinitionResponse:
    out: GetWorkflowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.arn required")
    if data.get("createdAt") is not None:
        import capo_nova_act.types.date_timestamp

        out["created_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.created_at required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("exportConfig") is not None:
        import capo_nova_act.types.workflow_export_config

        out["export_config"] = (
            capo_nova_act.types.workflow_export_config.deserialize_json(
                data["exportConfig"]
            )
        )
    if data.get("status") is not None:
        import capo_nova_act.types.workflow_definition_status

        out["status"] = capo_nova_act.types.workflow_definition_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetWorkflowDefinitionResponse.status required")
    return out


def redact_sensitive(value: GetWorkflowDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
