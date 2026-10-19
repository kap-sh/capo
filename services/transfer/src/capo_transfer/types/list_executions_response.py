"""Generated from Smithy shape ``com.amazonaws.transfer#ListExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_executions
    import capo_transfer.types.next_token
    import capo_transfer.types.workflow_id


class ListExecutionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p> <code>ListExecutions</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional executions.</p>"""
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    executions: "capo_transfer.types.listed_executions.ListedExecutions"
    """<p>Returns the details for each execution, in a <code>ListedExecution</code> array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExecutionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["WorkflowId"] = value["workflow_id"]
    import capo_transfer.types.listed_executions

    out["Executions"] = capo_transfer.types.listed_executions.serialize_aws_json_1_1(
        value["executions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExecutionsResponse:
    out: ListExecutionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("Executions") is not None:
        import capo_transfer.types.listed_executions

        out["executions"] = (
            capo_transfer.types.listed_executions.deserialize_aws_json_1_1(
                data["Executions"]
            )
        )
    else:
        out["executions"] = []
    return out
