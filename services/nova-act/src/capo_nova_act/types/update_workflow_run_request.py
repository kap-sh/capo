"""Generated from Smithy shape ``com.amazonaws.novaact#UpdateWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_run_status


class UpdateWorkflowRunRequest(TypedDict, closed=True):
    workflow_definition_name: (
        "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName"
    )
    """<p>The name of the workflow definition containing the workflow run.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run to update.</p>"""
    status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The new status to set for the workflow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowRunRequest) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_run_status

    out["status"] = capo_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkflowRunRequest:
    out: UpdateWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_nova_act.types.workflow_run_status

        out["status"] = capo_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_nova_act.types.workflow_run_status.WorkflowRunStatus", ""
        )
    return out
