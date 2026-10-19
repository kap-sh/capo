"""Generated from Smithy shape ``com.amazonaws.swf#TerminateWorkflowExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.child_policy
    import capo_swf.types.data
    import capo_swf.types.domain_name
    import capo_swf.types.terminate_reason
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional


class TerminateWorkflowExecutionInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The domain of the workflow execution to terminate.</p>"""
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The workflowId of the workflow execution to terminate.</p>"""
    run_id: NotRequired["capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"]
    """<p>The runId of the workflow execution to terminate.</p>"""
    reason: NotRequired["capo_swf.types.terminate_reason.TerminateReason"]
    """<p> A descriptive reason for terminating the workflow execution.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p> Details for terminating the workflow execution.</p>"""
    child_policy: NotRequired["capo_swf.types.child_policy.ChildPolicy"]
    """<p>If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TerminateWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["workflowId"] = value["workflow_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    if "child_policy" in value:
        import capo_swf.types.child_policy

        out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
            value["child_policy"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TerminateWorkflowExecutionInput:
    out: TerminateWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
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
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("details") is not None:
        out["details"] = data["details"]
    if data.get("childPolicy") is not None:
        import capo_swf.types.child_policy

        out["child_policy"] = capo_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    return out
