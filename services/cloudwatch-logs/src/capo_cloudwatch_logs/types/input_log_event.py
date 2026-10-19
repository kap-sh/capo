"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InputLogEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.event_message
    import capo_cloudwatch_logs.types.timestamp


class InputLogEvent(TypedDict, closed=True):
    timestamp: "capo_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The time the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    message: "capo_cloudwatch_logs.types.event_message.EventMessage"
    """<p>The raw event message. Each log event can be no larger than 1 MB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLogEvent) -> dict:
    out: dict = {}
    out["timestamp"] = value["timestamp"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLogEvent:
    out: InputLogEvent = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    else:
        out["timestamp"] = 0
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
