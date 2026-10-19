"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_mode_details
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.stream_status
    import capo_kinesis.types.timestamp


class StreamSummary(TypedDict, closed=True):
    stream_name: "capo_kinesis.types.stream_name.StreamName"
    """<p>The name of a stream.</p>"""
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the stream.</p>"""
    stream_status: "capo_kinesis.types.stream_status.StreamStatus"
    """<p>The status of the stream.</p>"""
    stream_mode_details: NotRequired[
        "capo_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    stream_creation_timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The timestamp at which the stream was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamSummary) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    out["StreamARN"] = value["stream_arn"]
    import capo_kinesis.types.stream_status

    out["StreamStatus"] = capo_kinesis.types.stream_status.serialize_aws_json_1_1(
        value["stream_status"]
    )
    if "stream_mode_details" in value:
        import capo_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            capo_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    if "stream_creation_timestamp" in value:
        import capo_kinesis.types.timestamp

        out["StreamCreationTimestamp"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["stream_creation_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamSummary:
    out: StreamSummary = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    else:
        out["stream_name"] = ""
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("StreamStatus") is not None:
        import capo_kinesis.types.stream_status

        out["stream_status"] = (
            capo_kinesis.types.stream_status.deserialize_aws_json_1_1(
                data["StreamStatus"]
            )
        )
    else:
        import typing

        out["stream_status"] = typing.cast(
            "capo_kinesis.types.stream_status.StreamStatus", ""
        )
    if data.get("StreamModeDetails") is not None:
        import capo_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            capo_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if data.get("StreamCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    return out
