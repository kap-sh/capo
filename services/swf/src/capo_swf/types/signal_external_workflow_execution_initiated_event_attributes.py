"""Generated from Smithy shape ``com.amazonaws.swf#SignalExternalWorkflowExecutionInitiatedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.signal_name
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class SignalExternalWorkflowExecutionInitiatedEventAttributes(TypedDict, closed=True):
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The <code>workflowId</code> of the external workflow execution.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The <code>runId</code> of the external workflow execution to send the signal to.</p>"""
    signal_name: "capo_swf.types.signal_name.SignalName"
    """<p>The name of the signal.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The input provided to the signal.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>SignalExternalWorkflowExecution</code> decision for this signal. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent decision tasks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: SignalExternalWorkflowExecutionInitiatedEventAttributes,
) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    if "control" in value:
        out["control"] = value["control"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> SignalExternalWorkflowExecutionInitiatedEventAttributes:
    out: SignalExternalWorkflowExecutionInitiatedEventAttributes = {}  # type: ignore[typeddict-item]
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
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("control") is not None:
        out["control"] = data["control"]
    return out
