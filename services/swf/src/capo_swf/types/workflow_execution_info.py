"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.canceled
    import capo_swf.types.close_status
    import capo_swf.types.execution_status
    import capo_swf.types.tag_list
    import capo_swf.types.timestamp
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_type


class WorkflowExecutionInfo(TypedDict, closed=True):
    execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The workflow execution this information is about.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The type of the workflow execution.</p>"""
    start_timestamp: "capo_swf.types.timestamp.Timestamp"
    """<p>The time when the execution was started.</p>"""
    close_timestamp: NotRequired["capo_swf.types.timestamp.Timestamp"]
    """<p>The time when the workflow execution was closed. Set only if the execution status is CLOSED.</p>"""
    execution_status: "capo_swf.types.execution_status.ExecutionStatus"
    """<p>The current status of the execution.</p>"""
    close_status: NotRequired["capo_swf.types.close_status.CloseStatus"]
    """<p>If the execution status is closed then this specifies how the execution was closed:</p> <ul> <li> <p> <code>COMPLETED</code> – the execution was successfully completed.</p> </li> <li> <p> <code>CANCELED</code> – the execution was canceled.Cancellation allows the implementation to gracefully clean up before the execution is closed.</p> </li> <li> <p> <code>TERMINATED</code> – the execution was force terminated.</p> </li> <li> <p> <code>FAILED</code> – the execution failed to complete.</p> </li> <li> <p> <code>TIMED_OUT</code> – the execution did not complete in the alloted time and was automatically timed out.</p> </li> <li> <p> <code>CONTINUED_AS_NEW</code> – the execution is logically continued. This means the current execution was completed and a new execution was started to carry on the workflow.</p> </li> </ul>"""
    parent: NotRequired["capo_swf.types.workflow_execution.WorkflowExecution"]
    """<p>If this workflow execution is a child of another execution then contains the workflow execution that started this execution.</p>"""
    tag_list: NotRequired["capo_swf.types.tag_list.TagList"]
    """<p>The list of tags associated with the workflow execution. Tags can be used to identify and list workflow executions of interest through the visibility APIs. A workflow execution can have a maximum of 5 tags.</p>"""
    cancel_requested: "capo_swf.types.canceled.Canceled"
    """<p>Set to true if a cancellation is requested for this workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionInfo) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_execution

    out["execution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["execution"]
    )
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    import capo_swf.types.timestamp

    out["startTimestamp"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
        value["start_timestamp"]
    )
    if "close_timestamp" in value:
        import capo_swf.types.timestamp

        out["closeTimestamp"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
            value["close_timestamp"]
        )
    import capo_swf.types.execution_status

    out["executionStatus"] = capo_swf.types.execution_status.serialize_aws_json_1_0(
        value["execution_status"]
    )
    if "close_status" in value:
        import capo_swf.types.close_status

        out["closeStatus"] = capo_swf.types.close_status.serialize_aws_json_1_0(
            value["close_status"]
        )
    if "parent" in value:
        import capo_swf.types.workflow_execution

        out["parent"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
            value["parent"]
        )
    if "tag_list" in value:
        import capo_swf.types.tag_list

        out["tagList"] = capo_swf.types.tag_list.serialize_aws_json_1_0(
            value["tag_list"]
        )
    out["cancelRequested"] = value.get("cancel_requested", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionInfo:
    out: WorkflowExecutionInfo = {}  # type: ignore[typeddict-item]
    if data.get("execution") is not None:
        import capo_swf.types.workflow_execution

        out["execution"] = capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
            data["execution"]
        )
    else:
        raise DeserializationError("WorkflowExecutionInfo.execution required")
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("WorkflowExecutionInfo.workflow_type required")
    if data.get("startTimestamp") is not None:
        import capo_swf.types.timestamp

        out["start_timestamp"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["startTimestamp"]
        )
    else:
        import datetime

        out["start_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("closeTimestamp") is not None:
        import capo_swf.types.timestamp

        out["close_timestamp"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["closeTimestamp"]
        )
    if data.get("executionStatus") is not None:
        import capo_swf.types.execution_status

        out["execution_status"] = (
            capo_swf.types.execution_status.deserialize_aws_json_1_0(
                data["executionStatus"]
            )
        )
    else:
        import typing

        out["execution_status"] = typing.cast(
            "capo_swf.types.execution_status.ExecutionStatus", ""
        )
    if data.get("closeStatus") is not None:
        import capo_swf.types.close_status

        out["close_status"] = capo_swf.types.close_status.deserialize_aws_json_1_0(
            data["closeStatus"]
        )
    if data.get("parent") is not None:
        import capo_swf.types.workflow_execution

        out["parent"] = capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
            data["parent"]
        )
    if data.get("tagList") is not None:
        import capo_swf.types.tag_list

        out["tag_list"] = capo_swf.types.tag_list.deserialize_aws_json_1_0(
            data["tagList"]
        )
    if data.get("cancelRequested") is not None:
        out["cancel_requested"] = data["cancelRequested"]
    else:
        out["cancel_requested"] = False
    return out
