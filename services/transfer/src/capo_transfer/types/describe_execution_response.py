"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_execution
    import capo_transfer.types.workflow_id


class DescribeExecutionResponse(TypedDict, closed=True):
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    execution: "capo_transfer.types.described_execution.DescribedExecution"
    """<p>The structure that contains the details of the workflow' execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExecutionResponse) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    import capo_transfer.types.described_execution

    out["Execution"] = capo_transfer.types.described_execution.serialize_aws_json_1_1(
        value["execution"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExecutionResponse:
    out: DescribeExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("Execution") is not None:
        import capo_transfer.types.described_execution

        out["execution"] = (
            capo_transfer.types.described_execution.deserialize_aws_json_1_1(
                data["Execution"]
            )
        )
    else:
        raise DeserializationError("DescribeExecutionResponse.execution required")
    return out
