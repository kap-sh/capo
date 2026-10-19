"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#TimestampSegment``."""

from typing_extensions import TypedDict


class TimestampSegment(TypedDict, closed=True):
    start_time_millis: "int"
    """Start timestamp in milliseconds"""
    end_time_millis: "int"
    """End timestamp in milliseconds"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampSegment) -> dict:
    out: dict = {}
    out["startTimeMillis"] = value["start_time_millis"]
    out["endTimeMillis"] = value["end_time_millis"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampSegment:
    out: TimestampSegment = {}  # type: ignore[typeddict-item]
    if data.get("startTimeMillis") is not None:
        out["start_time_millis"] = data["startTimeMillis"]
    else:
        out["start_time_millis"] = 0
    if data.get("endTimeMillis") is not None:
        out["end_time_millis"] = data["endTimeMillis"]
    else:
        out["end_time_millis"] = 0
    return out
