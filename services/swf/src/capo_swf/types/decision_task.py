"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.history_event_list
    import capo_swf.types.page_token
    import capo_swf.types.task_token
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_type


class DecisionTask(TypedDict, closed=True):
    task_token: "capo_swf.types.task_token.TaskToken"
    """<p>The opaque string used as a handle on the task. This token is used by workers to communicate progress and response information back to the system about the task.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskStarted</code> event recorded in the history.</p>"""
    workflow_execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The workflow execution for which this decision task was created.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The type of the workflow execution for which this decision task was created.</p>"""
    events: "capo_swf.types.history_event_list.HistoryEventList"
    """<p>A paginated list of history events of the workflow execution. The decider uses this during the processing of the decision task.</p>"""
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If a <code>NextPageToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>nextPageToken</code>. Keep all other arguments unchanged.</p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call.</p>"""
    previous_started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the DecisionTaskStarted event of the previous decision task of this workflow execution that was processed by the decider. This can be used to determine the events in the history new since the last decision task received by the decider.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTask) -> dict:
    out: dict = {}
    out["taskToken"] = value["task_token"]
    out["startedEventId"] = value.get("started_event_id", 0)
    import capo_swf.types.workflow_execution

    out["workflowExecution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["workflow_execution"]
    )
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    import capo_swf.types.history_event_list

    out["events"] = capo_swf.types.history_event_list.serialize_aws_json_1_0(
        value["events"]
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["previousStartedEventId"] = value.get("previous_started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTask:
    out: DecisionTask = {}  # type: ignore[typeddict-item]
    if data.get("taskToken") is not None:
        out["task_token"] = data["taskToken"]
    else:
        out["task_token"] = ""
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
        raise DeserializationError("DecisionTask.workflow_execution required")
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("DecisionTask.workflow_type required")
    if data.get("events") is not None:
        import capo_swf.types.history_event_list

        out["events"] = capo_swf.types.history_event_list.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    if data.get("previousStartedEventId") is not None:
        out["previous_started_event_id"] = data["previousStartedEventId"]
    else:
        out["previous_started_event_id"] = 0
    return out
