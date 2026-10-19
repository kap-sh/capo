"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelWorkflowExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class RequestCancelWorkflowExecutionInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution to cancel.</p>"""
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to cancel.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The runId of the workflow execution to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestCancelWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RequestCancelWorkflowExecutionInput:
    out: RequestCancelWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    return out
