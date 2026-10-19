"""Generated from Smithy shape ``com.amazonaws.transfer#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.listed_workflows
    import capo_transfer.types.next_token


class ListWorkflowsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p> <code>ListWorkflows</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional workflows.</p>"""
    workflows: "capo_transfer.types.listed_workflows.ListedWorkflows"
    """<p>Returns the <code>Arn</code>, <code>WorkflowId</code>, and <code>Description</code> for each workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.listed_workflows

    out["Workflows"] = capo_transfer.types.listed_workflows.serialize_aws_json_1_1(
        value["workflows"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Workflows") is not None:
        import capo_transfer.types.listed_workflows

        out["workflows"] = (
            capo_transfer.types.listed_workflows.deserialize_aws_json_1_1(
                data["Workflows"]
            )
        )
    else:
        out["workflows"] = []
    return out
