"""Generated from Smithy shape ``com.amazonaws.swf#StartChildWorkflowExecutionInitiatedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.arn
    import capo_swf.types.child_policy
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.event_id
    import capo_swf.types.tag_list
    import capo_swf.types.task_list
    import capo_swf.types.task_priority
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_type


class StartChildWorkflowExecutionInitiatedEventAttributes(TypedDict, closed=True):
    workflow_id: "capo_swf.types.workflow_id.WorkflowId"
    """<p>The <code>workflowId</code> of the child workflow execution.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The type of the child workflow execution.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that can be used by the decider in subsequent decision tasks. This data isn't sent to the activity.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The inputs provided to the child workflow execution.</p>"""
    execution_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration for the child workflow execution. If the workflow execution isn't closed within this duration, it is timed out and force-terminated.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The name of the task list used for the decision tasks of the child workflow execution.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p> The priority assigned for the decision tasks for this workflow execution. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>StartChildWorkflowExecution</code> <a>Decision</a> to request this child workflow execution. This information can be useful for diagnosing problems by tracing back the cause of events.</p>"""
    child_policy: "capo_swf.types.child_policy.ChildPolicy"
    """<p>The policy to use for the child workflow executions if this execution gets terminated by explicitly calling the <a>TerminateWorkflowExecution</a> action or due to an expired timeout.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration allowed for the decision tasks for this workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    tag_list: NotRequired["capo_swf.types.tag_list.TagList"]
    """<p>The list of tags to associated with the child workflow execution.</p>"""
    lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The IAM role to attach to the child workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: StartChildWorkflowExecutionInitiatedEventAttributes,
) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "execution_start_to_close_timeout" in value:
        out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    import capo_swf.types.child_policy

    out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    if "task_start_to_close_timeout" in value:
        out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    if "tag_list" in value:
        import capo_swf.types.tag_list

        out["tagList"] = capo_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> StartChildWorkflowExecutionInitiatedEventAttributes:
    out: StartChildWorkflowExecutionInitiatedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError(
            "StartChildWorkflowExecutionInitiatedEventAttributes.workflow_id required"
        )
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "StartChildWorkflowExecutionInitiatedEventAttributes.workflow_type required"
        )
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("executionStartToCloseTimeout") is not None:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError(
            "StartChildWorkflowExecutionInitiatedEventAttributes.task_list required"
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("childPolicy") is not None:
        import capo_swf.types.child_policy

        out["child_policy"] = capo_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        raise DeserializationError(
            "StartChildWorkflowExecutionInitiatedEventAttributes.child_policy required"
        )
    if data.get("taskStartToCloseTimeout") is not None:
        out["task_start_to_close_timeout"] = data["taskStartToCloseTimeout"]
    if data.get("tagList") is not None:
        import capo_swf.types.tag_list

        out["tag_list"] = capo_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if data.get("lambdaRole") is not None:
        out["lambda_role"] = data["lambdaRole"]
    return out
