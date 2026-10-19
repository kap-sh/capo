"""Generated from Smithy shape ``com.amazonaws.swf#SignalExternalWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.signal_name
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class SignalExternalWorkflowExecutionDecisionAttributes(TypedDict, closed=True):
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p> The <code>workflowId</code> of the workflow execution to be signaled.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The <code>runId</code> of the workflow execution to be signaled.</p>"""
    signal_name: "capo_swf.types.signal_name.SignalName"
    """<p> The name of the signal.The target workflow execution uses the signal name and input to process the signal.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p> The input data to be provided with the signal. The target workflow execution uses the signal name and input data to process the signal.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>The data attached to the event that can be used by the decider in subsequent decision tasks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: SignalExternalWorkflowExecutionDecisionAttributes,
) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    if "control" in value:
        out["control"] = value["control"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> SignalExternalWorkflowExecutionDecisionAttributes:
    out: SignalExternalWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
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
    if data.get("control") is not None:
        out["control"] = data["control"]
    return out
