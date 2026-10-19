"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionSignaledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.signal_name
    import capo_swf.types.workflow_execution


class WorkflowExecutionSignaledEventAttributes(TypedDict, closed=True):
    signal_name: "capo_swf.types.signal_name.SignalName"
    """<p>The name of the signal received. The decider can use the signal name and inputs to determine how to the process the signal.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The inputs provided with the signal. The decider can use the signal name and inputs to determine how to process the signal.</p>"""
    external_workflow_execution: NotRequired[
        "capo_swf.types.workflow_execution.WorkflowExecution"
    ]
    """<p>The workflow execution that sent the signal. This is set only of the signal was sent by another workflow execution.</p>"""
    external_initiated_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>SignalExternalWorkflowExecutionInitiated</code> event corresponding to the <code>SignalExternalWorkflow</code> decision to signal this workflow execution.The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event. This field is set only if the signal was initiated by another workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionSignaledEventAttributes) -> dict:
    out: dict = {}
    out["signalName"] = value["signal_name"]
    if "input" in value:
        out["input"] = value["input"]
    if "external_workflow_execution" in value:
        import capo_swf.types.workflow_execution

        out["externalWorkflowExecution"] = (
            capo_swf.types.workflow_execution.serialize_aws_json_1_0(
                value["external_workflow_execution"]
            )
        )
    out["externalInitiatedEventId"] = value.get("external_initiated_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionSignaledEventAttributes:
    out: WorkflowExecutionSignaledEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("signalName") is not None:
        out["signal_name"] = data["signalName"]
    else:
        out["signal_name"] = ""
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("externalWorkflowExecution") is not None:
        import capo_swf.types.workflow_execution

        out["external_workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["externalWorkflowExecution"]
            )
        )
    if data.get("externalInitiatedEventId") is not None:
        out["external_initiated_event_id"] = data["externalInitiatedEventId"]
    else:
        out["external_initiated_event_id"] = 0
    return out
