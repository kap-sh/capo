"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListWorkflowStepExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer
    import capo_imagebuilder.types.workflow_execution_id


class ListWorkflowStepExecutionsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>The maximum number of items to return in a single request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. Use the <code>nextToken</code> value from a previously truncated response.</p>"""
    workflow_execution_id: (
        "capo_imagebuilder.types.workflow_execution_id.WorkflowExecutionId"
    )
    """<p>The unique identifier that Image Builder assigned to keep track of runtime details when it ran the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowStepExecutionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["workflowExecutionId"] = value["workflow_execution_id"]
    return out


def deserialize_json(data: dict) -> ListWorkflowStepExecutionsRequest:
    out: ListWorkflowStepExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("workflowExecutionId") is not None:
        out["workflow_execution_id"] = data["workflowExecutionId"]
    else:
        out["workflow_execution_id"] = ""
    return out
