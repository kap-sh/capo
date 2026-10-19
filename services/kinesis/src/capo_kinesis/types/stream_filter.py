"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.timestamp


class StreamFilter(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) of the source stream to filter by.</p>"""
    stream_creation_timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The creation timestamp of the source stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamFilter) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "stream_creation_timestamp" in value:
        import capo_kinesis.types.timestamp

        out["StreamCreationTimestamp"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["stream_creation_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamFilter:
    out: StreamFilter = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("StreamCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    return out
