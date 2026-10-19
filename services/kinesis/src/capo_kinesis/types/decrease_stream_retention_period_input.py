"""Generated from Smithy shape ``com.amazonaws.kinesis#DecreaseStreamRetentionPeriodInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.retention_period_hours
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class DecreaseStreamRetentionPeriodInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to modify.</p>"""
    retention_period_hours: (
        "capo_kinesis.types.retention_period_hours.RetentionPeriodHours"
    )
    """<p>The new retention period of the stream, in hours. Must be less than the current retention period.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecreaseStreamRetentionPeriodInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["RetentionPeriodHours"] = value["retention_period_hours"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DecreaseStreamRetentionPeriodInput:
    out: DecreaseStreamRetentionPeriodInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("RetentionPeriodHours") is not None:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        out["retention_period_hours"] = 0
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
