"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.workflow_id


class DescribeWorkflowRequest(TypedDict, closed=True):
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkflowRequest) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkflowRequest:
    out: DescribeWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    return out
