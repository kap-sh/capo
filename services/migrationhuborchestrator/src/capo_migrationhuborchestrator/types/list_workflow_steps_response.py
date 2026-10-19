"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.workflow_steps_summary_list


class ListWorkflowStepsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    workflow_steps_summary: "capo_migrationhuborchestrator.types.workflow_steps_summary_list.WorkflowStepsSummaryList"
    """<p>The summary of steps in a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_migrationhuborchestrator.types.workflow_steps_summary_list

    out["workflowStepsSummary"] = (
        capo_migrationhuborchestrator.types.workflow_steps_summary_list.serialize_json(
            value["workflow_steps_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowStepsResponse:
    out: ListWorkflowStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workflowStepsSummary") is not None:
        import capo_migrationhuborchestrator.types.workflow_steps_summary_list

        out["workflow_steps_summary"] = (
            capo_migrationhuborchestrator.types.workflow_steps_summary_list.deserialize_json(
                data["workflowStepsSummary"]
            )
        )
    else:
        out["workflow_steps_summary"] = []
    return out
