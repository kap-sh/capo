"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateStreamWarmThroughputInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.natural_integer_object
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class UpdateStreamWarmThroughputInput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream to be updated.</p>"""
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to be updated.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    warm_throughput_mi_bps: (
        "capo_kinesis.types.natural_integer_object.NaturalIntegerObject"
    )
    """<p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamWarmThroughputInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["WarmThroughputMiBps"] = value["warm_throughput_mi_bps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamWarmThroughputInput:
    out: UpdateStreamWarmThroughputInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("WarmThroughputMiBps") is not None:
        out["warm_throughput_mi_bps"] = data["WarmThroughputMiBps"]
    else:
        out["warm_throughput_mi_bps"] = 0
    return out
