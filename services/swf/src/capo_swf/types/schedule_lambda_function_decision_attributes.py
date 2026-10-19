"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleLambdaFunctionDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.function_id
    import capo_swf.types.function_input
    import capo_swf.types.function_name


class ScheduleLambdaFunctionDecisionAttributes(TypedDict, closed=True):
    id: "capo_swf.types.function_id.FunctionId"
    """<p>A string that identifies the Lambda function execution in the event history.</p>"""
    name: "capo_swf.types.function_name.FunctionName"
    """<p>The name, or ARN, of the Lambda function to schedule.</p>"""
    control: NotRequired["capo_swf.types.data.Data"]
    """<p>The data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.</p>"""
    input: NotRequired["capo_swf.types.function_input.FunctionInput"]
    """<p>The optional input data to be supplied to the Lambda function.</p>"""
    start_to_close_timeout: NotRequired[
        "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The timeout value, in seconds, after which the Lambda function is considered to be failed once it has started. This can be any integer from 1-900 (1s-15m).</p> <p>If no value is supplied, then a default value of 900s is assumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleLambdaFunctionDecisionAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleLambdaFunctionDecisionAttributes:
    out: ScheduleLambdaFunctionDecisionAttributes = {}  # type: ignore[typeddict-item]
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
    return out
