"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.activity_id
    import capo_swf.types.activity_type
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.task_token
    import capo_swf.types.workflow_execution


class ActivityTask(TypedDict, closed=True):
    task_token: "capo_swf.types.task_token.TaskToken"
    """<p>The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.</p>"""
    activity_id: "capo_swf.types.activity_id.ActivityId"
    """<p>The unique ID of the task.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event recorded in the history.</p>"""
    workflow_execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The workflow execution that started this activity task.</p>"""
    activity_type: "capo_swf.types.activity_type.ActivityType"
    """<p>The type of this activity task.</p>"""
    input: NotRequired["capo_swf.types.data.Data"]
    """<p>The inputs provided when the activity task was scheduled. The form of the input is user defined and should be meaningful to the activity implementation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTask) -> dict:
    out: dict = {}
    out["taskToken"] = value["task_token"]
    out["activityId"] = value["activity_id"]
    out["startedEventId"] = value.get("started_event_id", 0)
    import capo_swf.types.workflow_execution

    out["workflowExecution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["workflow_execution"]
    )
    import capo_swf.types.activity_type

    out["activityType"] = capo_swf.types.activity_type.serialize_aws_json_1_0(
        value["activity_type"]
    )
    if "input" in value:
        out["input"] = value["input"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTask:
    out: ActivityTask = {}  # type: ignore[typeddict-item]
    if data.get("taskToken") is not None:
        out["task_token"] = data["taskToken"]
    else:
        out["task_token"] = ""
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        out["activity_id"] = ""
    if data.get("startedEventId") is not None:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if data.get("workflowExecution") is not None:
        import capo_swf.types.workflow_execution

        out["workflow_execution"] = (
            capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
                data["workflowExecution"]
            )
        )
    else:
        raise DeserializationError("ActivityTask.workflow_execution required")
    if data.get("activityType") is not None:
        import capo_swf.types.activity_type

        out["activity_type"] = capo_swf.types.activity_type.deserialize_aws_json_1_0(
            data["activityType"]
        )
    else:
        raise DeserializationError("ActivityTask.activity_type required")
    if data.get("input") is not None:
        out["input"] = data["input"]
    return out
