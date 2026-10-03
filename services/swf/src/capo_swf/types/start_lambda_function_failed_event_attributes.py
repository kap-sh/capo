"""Generated from Smithy shape ``com.amazonaws.swf#StartLambdaFunctionFailedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.cause_message
    import capo_swf.types.event_id
    import capo_swf.types.start_lambda_function_failed_cause


class StartLambdaFunctionFailedEventAttributes(TypedDict, closed=True):
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    cause: NotRequired[
        "capo_swf.types.start_lambda_function_failed_cause.StartLambdaFunctionFailedCause"
    ]
    """<p>The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p> <note> <p>If <code>cause</code> is set to <code>OPERATION_NOT_PERMITTED</code>, the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html">Lambda Tasks</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""
    message: NotRequired["capo_swf.types.cause_message.CauseMessage"]
    """<p>A description that can help diagnose the cause of the fault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartLambdaFunctionFailedEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    if "cause" in value:
        import capo_swf.types.start_lambda_function_failed_cause

        out["cause"] = (
            capo_swf.types.start_lambda_function_failed_cause.serialize_aws_json_1_0(
                value["cause"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartLambdaFunctionFailedEventAttributes:
    out: StartLambdaFunctionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("scheduledEventId") is not None:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if data.get("cause") is not None:
        import capo_swf.types.start_lambda_function_failed_cause

        out["cause"] = (
            capo_swf.types.start_lambda_function_failed_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
