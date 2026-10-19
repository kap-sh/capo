"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionContinuedAsNewEventAttributes``."""

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
    import capo_swf.types.workflow_run_id
    import capo_swf.types.workflow_type


class WorkflowExecutionContinuedAsNewEventAttributes(TypedDict, closed=True):
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The input provided to the new workflow execution.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>ContinueAsNewWorkflowExecution</code> decision that started this execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    new_execution_run_id: "capo_swf.types.workflow_run_id.WorkflowRunId"
    """<p>The <code>runId</code> of the new workflow execution.</p>"""
    execution_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The total duration allowed for the new workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The task list to use for the decisions of the new (continued) workflow execution.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p>The priority of the task to use for the decisions of the new (continued) workflow execution.</p>"""
    task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration of decision tasks for the new workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    child_policy: "capo_swf.types.child_policy.ChildPolicy"
    """<p>The policy to use for the child workflow executions of the new execution if it is terminated by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    tag_list: NotRequired["capo_swf.types.tag_list.TagList"]
    """<p>The list of tags associated with the new workflow execution.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type of this execution.</p>"""
    lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The IAM role to attach to the new (continued) workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: WorkflowExecutionContinuedAsNewEventAttributes,
) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    out["newExecutionRunId"] = value["new_execution_run_id"]
    if "execution_start_to_close_timeout" in value:
        out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    if "task_start_to_close_timeout" in value:
        out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    import capo_swf.types.child_policy

    out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    if "tag_list" in value:
        import capo_swf.types.tag_list

        out["tagList"] = capo_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> WorkflowExecutionContinuedAsNewEventAttributes:
    out: WorkflowExecutionContinuedAsNewEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    if data.get("newExecutionRunId") is not None:
        out["new_execution_run_id"] = data["newExecutionRunId"]
    else:
        out["new_execution_run_id"] = ""
    if data.get("executionStartToCloseTimeout") is not None:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionContinuedAsNewEventAttributes.task_list required"
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("taskStartToCloseTimeout") is not None:
        out["task_start_to_close_timeout"] = data["taskStartToCloseTimeout"]
    if data.get("childPolicy") is not None:
        import capo_swf.types.child_policy

        out["child_policy"] = capo_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        import typing

        out["child_policy"] = typing.cast("capo_swf.types.child_policy.ChildPolicy", "")
    if data.get("tagList") is not None:
        import capo_swf.types.tag_list

        out["tag_list"] = capo_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionContinuedAsNewEventAttributes.workflow_type required"
        )
    if data.get("lambdaRole") is not None:
        out["lambda_role"] = data["lambdaRole"]
    return out
