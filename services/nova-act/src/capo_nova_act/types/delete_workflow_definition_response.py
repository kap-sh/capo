"""Generated from Smithy shape ``com.amazonaws.novaact#DeleteWorkflowDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.workflow_definition_status


class DeleteWorkflowDefinitionResponse(TypedDict, closed=True):
    status: "capo_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus"
    """<p>The status of the workflow definition after deletion request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkflowDefinitionResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_definition_status

    out["status"] = capo_nova_act.types.workflow_definition_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteWorkflowDefinitionResponse:
    out: DeleteWorkflowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_nova_act.types.workflow_definition_status

        out["status"] = capo_nova_act.types.workflow_definition_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_nova_act.types.workflow_definition_status.WorkflowDefinitionStatus",
            "",
        )
    return out
