"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.execution_id
    import capo_transfer.types.workflow_id


class DescribeExecutionRequest(TypedDict, closed=True):
    execution_id: "capo_transfer.types.execution_id.ExecutionId"
    """<p>A unique identifier for the execution of a workflow.</p>"""
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExecutionRequest) -> dict:
    out: dict = {}
    out["ExecutionId"] = value["execution_id"]
    out["WorkflowId"] = value["workflow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExecutionRequest:
    out: DescribeExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    else:
        out["execution_id"] = ""
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    return out
