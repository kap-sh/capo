"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListTaskInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.workflow_arn


class ListTaskInstancesRequest(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>"""
    run_id: "capo_mwaa_serverless.types.id_string.IdString"
    """<p>The unique identifier of the workflow run for which you want a list of task instances.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of task instances to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListTaskInstances</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTaskInstancesRequest) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    out["RunId"] = value["run_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTaskInstancesRequest:
    out: ListTaskInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
