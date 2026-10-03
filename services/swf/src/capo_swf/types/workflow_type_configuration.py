"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.arn
    import capo_swf.types.child_policy
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.task_list
    import capo_swf.types.task_priority


class WorkflowTypeConfiguration(TypedDict, closed=True):
    default_task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum duration, specified when registering the workflow type, that a decision task for executions of this workflow type might take before returning completion or failure. If the task doesn'tdo close in the specified time then the task is automatically timed out and rescheduled. If the decider eventually reports a completion or failure, it is ignored. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_execution_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p> The default maximum duration, specified when registering the workflow type, for executions of this workflow type. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_task_list: NotRequired["capo_swf.types.task_list.TaskList"]
    """<p> The default task list, specified when registering the workflow type, for decisions tasks scheduled for workflow executions of this type. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p>"""
    default_task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> The default task priority, specified when registering the workflow type, for all decision tasks of this workflow type. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> decision.</p> <p>Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    default_child_policy: NotRequired["capo_swf.types.child_policy.ChildPolicy"]
    """<p> The default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    default_lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The default IAM role attached to this workflow type.</p> <note> <p>Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't specify an IAM role when starting this workflow type, the default Lambda role is attached to the execution. For more information, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html">https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowTypeConfiguration) -> dict:
    out: dict = {}
    if "default_task_start_to_close_timeout" in value:
        out["defaultTaskStartToCloseTimeout"] = value[
            "default_task_start_to_close_timeout"
        ]
    if "default_execution_start_to_close_timeout" in value:
        out["defaultExecutionStartToCloseTimeout"] = value[
            "default_execution_start_to_close_timeout"
        ]
    if "default_task_list" in value:
        import capo_swf.types.task_list

        out["defaultTaskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
            value["default_task_list"]
        )
    if "default_task_priority" in value:
        out["defaultTaskPriority"] = value["default_task_priority"]
    if "default_child_policy" in value:
        import capo_swf.types.child_policy

        out["defaultChildPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
            value["default_child_policy"]
        )
    if "default_lambda_role" in value:
        out["defaultLambdaRole"] = value["default_lambda_role"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowTypeConfiguration:
    out: WorkflowTypeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("defaultTaskStartToCloseTimeout") is not None:
        out["default_task_start_to_close_timeout"] = data[
            "defaultTaskStartToCloseTimeout"
        ]
    if data.get("defaultExecutionStartToCloseTimeout") is not None:
        out["default_execution_start_to_close_timeout"] = data[
            "defaultExecutionStartToCloseTimeout"
        ]
    if data.get("defaultTaskList") is not None:
        import capo_swf.types.task_list

        out["default_task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["defaultTaskList"]
        )
    if data.get("defaultTaskPriority") is not None:
        out["default_task_priority"] = data["defaultTaskPriority"]
    if data.get("defaultChildPolicy") is not None:
        import capo_swf.types.child_policy

        out["default_child_policy"] = (
            capo_swf.types.child_policy.deserialize_aws_json_1_0(
                data["defaultChildPolicy"]
            )
        )
    if data.get("defaultLambdaRole") is not None:
        out["default_lambda_role"] = data["defaultLambdaRole"]
    return out
