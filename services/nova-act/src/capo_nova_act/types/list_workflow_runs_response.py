"""Generated from Smithy shape ``com.amazonaws.novaact#ListWorkflowRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.next_token
    import capo_nova_act.types.workflow_run_summaries


class ListWorkflowRunsResponse(TypedDict, closed=True):
    workflow_run_summaries: (
        "capo_nova_act.types.workflow_run_summaries.WorkflowRunSummaries"
    )
    """<p>A list of summary information for workflow runs.</p>"""
    next_token: NotRequired["capo_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowRunsResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.workflow_run_summaries

    out["workflowRunSummaries"] = (
        capo_nova_act.types.workflow_run_summaries.serialize_json(
            value["workflow_run_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkflowRunsResponse:
    out: ListWorkflowRunsResponse = {}  # type: ignore[typeddict-item]
    if data.get("workflowRunSummaries") is not None:
        import capo_nova_act.types.workflow_run_summaries

        out["workflow_run_summaries"] = (
            capo_nova_act.types.workflow_run_summaries.deserialize_json(
                data["workflowRunSummaries"]
            )
        )
    else:
        out["workflow_run_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
