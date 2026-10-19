"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.workflow_arn


class GetWorkflowRunRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>"""
    run_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowRunRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowRunRequest:
    out: GetWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out
