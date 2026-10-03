"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.arn
    import capo_swf.types.child_policy
    import capo_swf.types.duration_in_seconds
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class WorkflowExecutionConfiguration(TypedDict, closed=True):
    task_start_to_close_timeout: "capo_swf.types.duration_in_seconds.DurationInSeconds"
    """<p>The maximum duration allowed for decision tasks for this workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    execution_start_to_close_timeout: (
        "capo_swf.types.duration_in_seconds.DurationInSeconds"
    )
    """<p>The total duration for this workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The task list used for the decision tasks generated for this workflow execution.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p>The priority assigned to decision tasks for this workflow execution. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    child_policy: "capo_swf.types.child_policy.ChildPolicy"
    """<p>The policy to use for the child workflow executions if this workflow execution is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The IAM role attached to the child workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionConfiguration) -> dict:
    out: dict = {}
    out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    import capo_swf.types.child_policy

    out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionConfiguration:
    out: WorkflowExecutionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("taskStartToCloseTimeout") is not None:
        out["task_start_to_close_timeout"] = data["taskStartToCloseTimeout"]
    else:
        raise DeserializationError(
            "WorkflowExecutionConfiguration.task_start_to_close_timeout required"
        )
    if data.get("executionStartToCloseTimeout") is not None:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
    else:
        raise DeserializationError(
            "WorkflowExecutionConfiguration.execution_start_to_close_timeout required"
        )
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError("WorkflowExecutionConfiguration.task_list required")
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("childPolicy") is not None:
        import capo_swf.types.child_policy

        out["child_policy"] = capo_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionConfiguration.child_policy required"
        )
    if data.get("lambdaRole") is not None:
        out["lambda_role"] = data["lambdaRole"]
    return out
