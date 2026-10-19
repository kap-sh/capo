"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionStartedEventAttributes``."""

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
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_run_id_optional
    import capo_swf.types.workflow_type


class WorkflowExecutionStartedEventAttributes(TypedDict, closed=True):
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The input provided to the workflow execution.</p>"""
    execution_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration for this workflow execution.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum duration of decision tasks for this workflow type.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    child_policy: "capo_swf.types.child_policy.ChildPolicy"
    """<p>The policy to use for the child workflow executions if this workflow execution is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    task_list: "capo_swf.types.task_list.TaskList"
    """<p>The name of the task list for scheduling the decision tasks for this workflow execution.</p>"""
    task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p>The priority of the decision tasks in the workflow execution.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type of this execution.</p>"""
    tag_list: NotRequired["capo_swf.types.tag_list.TagList"]
    """<p>The list of tags associated with this workflow execution. An execution can have up to 5 tags.</p>"""
    continued_execution_run_id: NotRequired[
        "capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
    ]
    """<p>If this workflow execution was started due to a <code>ContinueAsNewWorkflowExecution</code> decision, then it contains the <code>runId</code> of the previous workflow execution that was closed and continued as this execution.</p>"""
    parent_workflow_execution: NotRequired[
        "capo_swf.types.workflow_execution.WorkflowExecution"
    ]
    """<p>The source workflow execution that started this workflow execution. The member isn't set if the workflow execution was not started by a workflow.</p>"""
    parent_initiated_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>StartChildWorkflowExecutionInitiated</code> event corresponding to the <code>StartChildWorkflowExecution</code> <a>Decision</a> to start this workflow execution. The source event with this ID can be found in the history of the source workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The IAM role attached to the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionStartedEventAttributes) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "execution_start_to_close_timeout" in value:
        out["executionStartToCloseTimeout"] = value["execution_start_to_close_timeout"]
    if "task_start_to_close_timeout" in value:
        out["taskStartToCloseTimeout"] = value["task_start_to_close_timeout"]
    import capo_swf.types.child_policy

    out["childPolicy"] = capo_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    import capo_swf.types.task_list

    out["taskList"] = capo_swf.types.task_list.serialize_aws_json_1_0(
        value["task_list"]
    )
    if "task_priority" in value:
        out["taskPriority"] = value["task_priority"]
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    if "tag_list" in value:
        import capo_swf.types.tag_list

        out["tagList"] = capo_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    if "continued_execution_run_id" in value:
        out["continuedExecutionRunId"] = value["continued_execution_run_id"]
    if "parent_workflow_execution" in value:
        import capo_swf.types.workflow_execution

        out["parentWorkflowExecution"] = (
            capo_swf.types.workflow_execution.serialize_aws_json_1_0(
                value["parent_workflow_execution"]
            )
        )
    out["parentInitiatedEventId"] = value.get("parent_initiated_event_id", 0)
    if "lambda_role" in value:
        out["lambdaRole"] = value["lambda_role"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionStartedEventAttributes:
    out: WorkflowExecutionStartedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("executionStartToCloseTimeout") is not None:
        out["execution_start_to_close_timeout"] = data["executionStartToCloseTimeout"]
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
    if data.get("taskList") is not None:
        import capo_swf.types.task_list

        out["task_list"] = capo_swf.types.task_list.deserialize_aws_json_1_0(
            data["taskList"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionStartedEventAttributes.task_list required"
        )
    if data.get("taskPriority") is not None:
        out["task_priority"] = data["taskPriority"]
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionStartedEventAttributes.workflow_type required"
        )
    if data.get("tagList") is not None:
        import capo_swf.types.tag_list

        out["tag_list"] = capo_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if data.get("continuedExecutionRunId") is not None:
        out["continued_execution_run_id"] = data["continuedExecutionRunId"]
    if data.get("parentWorkflowExecution") is not None:
        import capo_swf.types.workflow_execution

        out["parent_workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["parentWorkflowExecution"]
            )
        )
    if data.get("parentInitiatedEventId") is not None:
        out["parent_initiated_event_id"] = data["parentInitiatedEventId"]
    else:
        out["parent_initiated_event_id"] = 0
    if data.get("lambdaRole") is not None:
        out["lambda_role"] = data["lambdaRole"]
    return out
