"""Generated from Smithy shape ``com.amazonaws.swf#RegisterWorkflowTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.arn
    import capo_swf.types.child_policy
    import capo_swf.types.description
    import capo_swf.types.domain_name
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.name
    import capo_swf.types.task_list
    import capo_swf.types.task_priority
    import capo_swf.types.version


class RegisterWorkflowTypeInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which to register the workflow type.</p>"""
    name: "capo_swf.types.name.Name"
    r"""<p>The name of the workflow type.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    version: "capo_swf.types.version.Version"
    r"""<p>The version of the workflow type.</p> <note> <p>The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the <a>ListWorkflowTypes</a> action.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>"""
    description: NotRequired["capo_swf.types.description.Description"]
    """<p>Textual description of the workflow type.</p>"""
    default_task_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>"""
    default_execution_start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the <a>StartWorkflowExecution</a> Action or <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for <code>defaultExecutionStartToCloseTimeout</code>; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit always causes the workflow execution to time out.</p>"""
    default_task_list: NotRequired["capo_swf.types.task_list.TaskList"]
    """<p>If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list isn't provided when starting the execution through the <a>StartWorkflowExecution</a> Action or <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p>"""
    default_task_priority: NotRequired["capo_swf.types.task_priority.TaskPriority"]
    """<p>The default task priority to assign to the workflow type. If not assigned, then <code>0</code> is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>"""
    default_child_policy: NotRequired["capo_swf.types.child_policy.ChildPolicy"]
    """<p>If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""
    default_lambda_role: NotRequired["capo_swf.types.arn.Arn"]
    """<p>The default IAM role attached to this workflow type.</p> <note> <p>Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't specify an IAM role when you start this workflow type, the default Lambda role is attached to the execution. For more information, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html">https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterWorkflowTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_aws_json_1_0(data: dict) -> RegisterWorkflowTypeInput:
    out: RegisterWorkflowTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("RegisterWorkflowTypeInput.domain required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisterWorkflowTypeInput.name required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("RegisterWorkflowTypeInput.version required")
    if data.get("description") is not None:
        out["description"] = data["description"]
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
