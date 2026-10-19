"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionScheduledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.event_id
    import capo_swf.types.function_id
    import capo_swf.types.function_input
    import capo_swf.types.function_name


class LambdaFunctionScheduledEventAttributes(TypedDict, closed=True):
    id: "capo_swf.types.function_id.FunctionId"
    """<p>The unique ID of the Lambda task.</p>"""
    name: "capo_swf.types.function_name.FunctionName"
    """<p>The name of the Lambda function.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>Data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.</p>"""
    input: NotRequired["capo_swf.types.function_input.FunctionInput"]
    """<p>The input provided to the Lambda task.</p>"""
    start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time a worker can take to process the Lambda task.</p>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionCompleted</code> event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionScheduledEventAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionScheduledEventAttributes:
    out: LambdaFunctionScheduledEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("control") is not None:
        out["control"] = data["control"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("startToCloseTimeout") is not None:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
