"""Generated from Smithy shape ``com.amazonaws.novaact#UpdateActRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.act_error
    import capo_nova_act.types.act_status
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name


class UpdateActRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the act.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing the act.</p>"""
    session_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing the act.</p>"""
    act_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act to update.</p>"""
    status: "capo_nova_act.types.act_status.ActStatus"
    """<p>The new status to set for the act.</p>"""
    error: NotRequired["capo_nova_act.types.act_error.ActError"]
    """<p>Error information to associate with the act, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActRequest) -> dict:
    out: dict = {}
    import capo_nova_act.types.act_status

    out["status"] = capo_nova_act.types.act_status.serialize_json(value["status"])
    if "error" in value:
        import capo_nova_act.types.act_error

        out["error"] = capo_nova_act.types.act_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> UpdateActRequest:
    out: UpdateActRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_nova_act.types.act_status

        out["status"] = capo_nova_act.types.act_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_nova_act.types.act_status.ActStatus", "")
    if data.get("error") is not None:
        import capo_nova_act.types.act_error

        out["error"] = capo_nova_act.types.act_error.deserialize_json(data["error"])
    return out


def redact_sensitive(value: UpdateActRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_nova_act.types.act_error

        out["error"] = capo_nova_act.types.act_error.redact_sensitive(value["error"])
    return out
