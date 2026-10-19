"""Generated from Smithy shape ``com.amazonaws.swf#ChildWorkflowExecutionTimedOutEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_execution_timeout_type
    import capo_swf.types.workflow_type


class ChildWorkflowExecutionTimedOutEventAttributes(TypedDict, closed=True):
    workflow_execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The child workflow execution that timed out.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The type of the child workflow execution.</p>"""
    timeout_type: (
        "capo_swf.types.workflow_execution_timeout_type.WorkflowExecutionTimeoutType"
    )
    """<p>The type of the timeout that caused the child workflow execution to time out.</p>"""
    initiated_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>StartChildWorkflowExecutionInitiated</code> event corresponding to the <code>StartChildWorkflowExecution</code> <a>Decision</a> to start this child workflow execution. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ChildWorkflowExecutionStarted</code> event recorded when this child workflow execution was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ChildWorkflowExecutionTimedOutEventAttributes,
) -> dict:
    out: dict = {}
    import capo_swf.types.workflow_execution

    out["workflowExecution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["workflow_execution"]
    )
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    import capo_swf.types.workflow_execution_timeout_type

    out["timeoutType"] = (
        capo_swf.types.workflow_execution_timeout_type.serialize_aws_json_1_0(
            value["timeout_type"]
        )
    )
    out["initiatedEventId"] = value.get("initiated_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ChildWorkflowExecutionTimedOutEventAttributes:
    out: ChildWorkflowExecutionTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("workflowExecution") is not None:
        import capo_swf.types.workflow_execution

        out["workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionTimedOutEventAttributes.workflow_execution required"
        )
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError(
            "ChildWorkflowExecutionTimedOutEventAttributes.workflow_type required"
        )
    if data.get("timeoutType") is not None:
        import capo_swf.types.workflow_execution_timeout_type

        out["timeout_type"] = (
            capo_swf.types.workflow_execution_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    else:
        import typing

        out["timeout_type"] = typing.cast(
            "capo_swf.types.workflow_execution_timeout_type.WorkflowExecutionTimeoutType",
            "",
        )
    if data.get("initiatedEventId") is not None:
        out["initiated_event_id"] = data["initiatedEventId"]
    else:
        out["initiated_event_id"] = 0
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    return out
