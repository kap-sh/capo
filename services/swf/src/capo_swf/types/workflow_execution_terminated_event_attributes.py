"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTerminatedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.child_policy
    import capo_swf.types.data
    import capo_swf.types.terminate_reason
    import capo_swf.types.workflow_execution_terminated_cause


class WorkflowExecutionTerminatedEventAttributes(TypedDict, closed=True):
    reason: NotRequired["capo_swf.types.terminate_reason.TerminateReason"]
    """<p>The reason provided for the termination.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>The details provided for the termination.</p>"""
    child_policy: "capo_swf.types.child_policy.ChildPolicy"
    """<p>The policy used for the child workflow executions of this workflow execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    cause: NotRequired[
        "capo_swf.types.workflow_execution_terminated_cause.WorkflowExecutionTerminatedCause"
    ]
    """<p>If set, indicates that the workflow execution was automatically terminated, and specifies the cause. This happens if the parent workflow execution times out or is terminated and the child policy is set to terminate child executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionTerminatedEventAttributes) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    import capo_swf.types.child_policy

    out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    if "cause" in value:
        import capo_swf.types.workflow_execution_terminated_cause

        out["cause"] = (
            capo_swf.types.workflow_execution_terminated_cause.serialize_aws_json_1_0(
                value["cause"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionTerminatedEventAttributes:
    out: WorkflowExecutionTerminatedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("details") is not None:
        out["details"] = data["details"]
    if data.get("childPolicy") is not None:
        import capo_swf.types.child_policy

        out["child_policy"] = capo_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        import typing

        out["child_policy"] = typing.cast("capo_swf.types.child_policy.ChildPolicy", "")
    if data.get("cause") is not None:
        import capo_swf.types.workflow_execution_terminated_cause

        out["cause"] = (
            capo_swf.types.workflow_execution_terminated_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    return out
