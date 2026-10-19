"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#DeleteWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_version


class DeleteWorkflowRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow you want to delete.</p>"""
    workflow_version: NotRequired[
        "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>Optional. The specific version of the workflow to delete. If not specified, all versions of the workflow are deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWorkflowRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWorkflowRequest:
    out: DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    return out
