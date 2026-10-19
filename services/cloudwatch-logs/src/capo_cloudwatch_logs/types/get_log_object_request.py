"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_object_pointer
    import capo_cloudwatch_logs.types.unmask


class GetLogObjectRequest(TypedDict, closed=True):
    unmask: NotRequired["capo_cloudwatch_logs.types.unmask.Unmask"]
    """<p>A boolean flag that indicates whether to unmask sensitive log data. When set to true, any masked or redacted data in the log object will be displayed in its original form. Default is false.</p>"""
    log_object_pointer: "capo_cloudwatch_logs.types.log_object_pointer.LogObjectPointer"
    """<p>A pointer to the specific log object to retrieve. This is a required parameter that uniquely identifies the log object within CloudWatch Logs. The pointer is typically obtained from a previous query or filter operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogObjectRequest) -> dict:
    out: dict = {}
    if "unmask" in value:
        out["unmask"] = value["unmask"]
    out["logObjectPointer"] = value["log_object_pointer"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogObjectRequest:
    out: GetLogObjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("unmask") is not None:
        out["unmask"] = data["unmask"]
    if data.get("logObjectPointer") is not None:
        out["log_object_pointer"] = data["logObjectPointer"]
    else:
        raise DeserializationError("GetLogObjectRequest.log_object_pointer required")
    return out
