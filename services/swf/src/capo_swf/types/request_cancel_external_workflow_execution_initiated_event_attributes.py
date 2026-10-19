"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelExternalWorkflowExecutionInitiatedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes(
    TypedDict, closed=True
):
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The <code>workflowId</code> of the external workflow execution to be canceled.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The <code>runId</code> of the external workflow execution to be canceled.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>RequestCancelExternalWorkflowExecution</code> decision for this cancellation request. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent workflow tasks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: RequestCancelExternalWorkflowExecutionInitiatedEventAttributes,
) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    if "control" in value:
        out["control"] = value["control"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> RequestCancelExternalWorkflowExecutionInitiatedEventAttributes:
    out: RequestCancelExternalWorkflowExecutionInitiatedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("control") is not None:
        out["control"] = data["control"]
    return out
