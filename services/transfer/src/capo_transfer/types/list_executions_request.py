"""Generated from Smithy shape ``com.amazonaws.transfer#ListExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.workflow_id


class ListExecutionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p> <code>ListExecutions</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional executions.</p> <p> This is useful for pagination, for instance. If you have 100 executions for a workflow, you might only want to list first 10. If so, call the API by specifying the <code>max-results</code>: </p> <p> <code>aws transfer list-executions --max-results 10</code> </p> <p> This returns details for the first 10 executions, as well as the pointer (<code>NextToken</code>) to the eleventh execution. You can now call the API again, supplying the <code>NextToken</code> value you received: </p> <p> <code>aws transfer list-executions --max-results 10 --next-token $somePointerReturnedFromPreviousListResult</code> </p> <p> This call returns the next 10 executions, the 11th through the 20th. You can then repeat the call until the details for all 100 executions have been returned. </p>"""
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExecutionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["WorkflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExecutionsRequest:
    out: ListExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    return out
