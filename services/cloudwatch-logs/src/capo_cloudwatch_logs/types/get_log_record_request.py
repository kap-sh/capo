"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_record_pointer
    import capo_cloudwatch_logs.types.unmask


class GetLogRecordRequest(TypedDict, closed=True):
    log_record_pointer: "capo_cloudwatch_logs.types.log_record_pointer.LogRecordPointer"
    """<p>The pointer corresponding to the log event record you want to retrieve. You get this from the response of a <code>GetQueryResults</code> operation. In that response, the value of the <code>@ptr</code> field for a log event is the value to use as <code>logRecordPointer</code> to retrieve that complete log event record.</p>"""
    unmask: NotRequired["capo_cloudwatch_logs.types.unmask.Unmask"]
    """<p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogRecordRequest) -> dict:
    out: dict = {}
    out["logRecordPointer"] = value["log_record_pointer"]
    if "unmask" in value:
        out["unmask"] = value["unmask"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogRecordRequest:
    out: GetLogRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("logRecordPointer") is not None:
        out["log_record_pointer"] = data["logRecordPointer"]
    else:
        raise DeserializationError("GetLogRecordRequest.log_record_pointer required")
    if data.get("unmask") is not None:
        out["unmask"] = data["unmask"]
    return out
