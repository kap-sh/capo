"""Generated from Smithy shape ``com.amazonaws.novaact#CreateWorkflowDefinitionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.client_token
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_description
    import capo_nova_act.types.workflow_export_config


class CreateWorkflowDefinitionRequest(TypedDict, closed=True):
    name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    """<p>The name of the workflow definition. Must be unique within your account and region.</p>"""
    description: NotRequired[
        "capo_nova_act.types.workflow_description.WorkflowDescription"
    ]
    """<p>An optional description of the workflow definition's purpose and functionality.</p>"""
    export_config: NotRequired[
        "capo_nova_act.types.workflow_export_config.WorkflowExportConfig"
    ]
    """<p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>"""
    client_token: NotRequired["capo_nova_act.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowDefinitionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "export_config" in value:
        import capo_nova_act.types.workflow_export_config

        out["exportConfig"] = capo_nova_act.types.workflow_export_config.serialize_json(
            value["export_config"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateWorkflowDefinitionRequest:
    out: CreateWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("exportConfig") is not None:
        import capo_nova_act.types.workflow_export_config

        out["export_config"] = (
            capo_nova_act.types.workflow_export_config.deserialize_json(
                data["exportConfig"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateWorkflowDefinitionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
