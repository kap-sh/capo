"""Generated from Smithy shape ``com.amazonaws.novaact#CreateActRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import capo_nova_act.types.client_token
    import capo_nova_act.types.task
    import capo_nova_act.types.tool_specs
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name


class CreateActRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the session.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the session.</p>"""
    session_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session to create the act in.</p>"""
    task: "capo_nova_act.types.task.Task"
    """<p>The task description that defines what the act should accomplish.</p>"""
    tool_specs: NotRequired["capo_nova_act.types.tool_specs.ToolSpecs"]
    """<p>A list of tool specifications that the act can invoke to complete its task.</p>"""
    client_token: NotRequired["capo_nova_act.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActRequest) -> dict:
    out: dict = {}
    out["task"] = value["task"]
    if "tool_specs" in value:
        import capo_nova_act.types.tool_specs

        out["toolSpecs"] = capo_nova_act.types.tool_specs.serialize_json(
            value["tool_specs"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateActRequest:
    out: CreateActRequest = {}  # type: ignore[typeddict-item]
    if data.get("task") is not None:
        out["task"] = data["task"]
    else:
        raise DeserializationError("CreateActRequest.task required")
    if data.get("toolSpecs") is not None:
        import capo_nova_act.types.tool_specs

        out["tool_specs"] = capo_nova_act.types.tool_specs.deserialize_json(
            data["toolSpecs"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateActRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "task" in value:
        out["task"] = "*** Sensitive Data Redacted ***"
    if "tool_specs" in value:
        import capo_nova_act.types.tool_specs

        out["tool_specs"] = capo_nova_act.types.tool_specs.redact_sensitive(
            value["tool_specs"]
        )
    return out
