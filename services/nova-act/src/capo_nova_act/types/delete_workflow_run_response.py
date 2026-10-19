"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.workflow_run_status


class DeleteWorkflowRunResponse(TypedDict, closed=True):
    status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The status of the workflow run after deletion request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowRunResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_run_status

    out["status"] = capo_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteWorkflowRunResponse:
    out: DeleteWorkflowRunResponse = {}  # type: ignore[typeddict-item]
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
