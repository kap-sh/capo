"""Generated from Smithy shape ``com.amazonaws.swf#SignalWorkflowExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.domain_name
    import capo_swf.types.signal_name
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class SignalWorkflowExecutionInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution to signal.</p>"""
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to signal.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The runId of the workflow execution to signal.</p>"""
    signal_name: "capo_swf.types.signal_name.SignalName"
    """<p>The name of the signal. This name must be meaningful to the target workflow.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>Data to attach to the <code>WorkflowExecutionSignaled</code> event in the target workflow execution's history.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalWorkflowExecutionInput:
    out: SignalWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("signalName") is not None:
        out["signal_name"] = data["signalName"]
    else:
        out["signal_name"] = ""
    if data.get("input") is not None:
        out["input"] = data["input"]
    return out
