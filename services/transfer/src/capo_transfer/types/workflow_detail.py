"""Generated from Smithy shape ``com.amazonaws.transfer#WorkflowDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.role
    import capo_transfer.types.workflow_id


class WorkflowDetail(TypedDict, closed=True):
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    execution_role: "capo_transfer.types.role.Role"
    """<p>Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowDetail) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    out["ExecutionRole"] = value["execution_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowDetail:
    out: WorkflowDetail = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("ExecutionRole") is not None:
        out["execution_role"] = data["ExecutionRole"]
    else:
        out["execution_role"] = ""
    return out
