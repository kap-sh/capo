"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateStreamModeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.natural_integer_object
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_mode_details


class UpdateStreamModeInput(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p> Specifies the ARN of the data stream whose capacity mode you want to update. </p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    stream_mode_details: "capo_kinesis.types.stream_mode_details.StreamModeDetails"
    """<p> Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams. </p>"""
    warm_throughput_mi_bps: NotRequired[
        "capo_kinesis.types.natural_integer_object.NaturalIntegerObject"
    ]
    """<p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations. This field is only valid when the stream mode is being updated to on-demand.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamModeInput) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    import capo_kinesis.types.stream_mode_details

    out["StreamModeDetails"] = (
        capo_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
            value["stream_mode_details"]
        )
    )
    if "warm_throughput_mi_bps" in value:
        out["WarmThroughputMiBps"] = value["warm_throughput_mi_bps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamModeInput:
    out: UpdateStreamModeInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("StreamModeDetails") is not None:
        import capo_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            capo_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    else:
        raise DeserializationError("UpdateStreamModeInput.stream_mode_details required")
    if data.get("WarmThroughputMiBps") is not None:
        out["warm_throughput_mi_bps"] = data["WarmThroughputMiBps"]
    return out
