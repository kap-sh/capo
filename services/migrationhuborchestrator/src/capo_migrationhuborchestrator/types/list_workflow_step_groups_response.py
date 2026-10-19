"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListWorkflowStepGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.next_token
    import capo_migrationhuborchestrator.types.workflow_step_groups_summary_list


class ListWorkflowStepGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_migrationhuborchestrator.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""
    workflow_step_groups_summary: "capo_migrationhuborchestrator.types.workflow_step_groups_summary_list.WorkflowStepGroupsSummaryList"
    """<p>The summary of step groups in a migration workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_migrationhuborchestrator.types.workflow_step_groups_summary_list

    out["workflowStepGroupsSummary"] = (
        capo_migrationhuborchestrator.types.workflow_step_groups_summary_list.serialize_json(
            value["workflow_step_groups_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListWorkflowStepGroupsResponse:
    out: ListWorkflowStepGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workflowStepGroupsSummary") is not None:
        import capo_migrationhuborchestrator.types.workflow_step_groups_summary_list

        out["workflow_step_groups_summary"] = (
            capo_migrationhuborchestrator.types.workflow_step_groups_summary_list.deserialize_json(
                data["workflowStepGroupsSummary"]
            )
        )
    else:
        out["workflow_step_groups_summary"] = []
    return out
