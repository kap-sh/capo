"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleLambdaFunctionFailedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.function_id
    import capo_swf.types.function_name
    import capo_swf.types.schedule_lambda_function_failed_cause


class ScheduleLambdaFunctionFailedEventAttributes(TypedDict, closed=True):
    id: "capo_swf.types.function_id.FunctionId"
    """<p>The ID provided in the <code>ScheduleLambdaFunction</code> decision that failed. </p>"""
    name: "capo_swf.types.function_name.FunctionName"
    """<p>The name of the Lambda function.</p>"""
    cause: "capo_swf.types.schedule_lambda_function_failed_cause.ScheduleLambdaFunctionFailedCause"
    """<p>The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p> <note> <p>If <code>cause</code> is set to <code>OPERATION_NOT_PERMITTED</code>, the decision failed because it lacked sufficient permissions. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""
    decision_task_completed_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionCompleted</code> event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleLambdaFunctionFailedEventAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_swf.types.schedule_lambda_function_failed_cause

    out["cause"] = (
        capo_swf.types.schedule_lambda_function_failed_cause.serialize_aws_json_1_0(
            value["cause"]
        )
    )
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleLambdaFunctionFailedEventAttributes:
    out: ScheduleLambdaFunctionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.name required"
        )
    if data.get("cause") is not None:
        import capo_swf.types.schedule_lambda_function_failed_cause

        out["cause"] = (
            capo_swf.types.schedule_lambda_function_failed_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.cause required"
        )
    if data.get("decisionTaskCompletedEventId") is not None:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
