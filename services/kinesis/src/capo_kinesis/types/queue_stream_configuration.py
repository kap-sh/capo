"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_starting_position
    import capo_kinesis.types.stream_arn


class QueueStreamConfiguration(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the data stream.</p>"""
    starting_position: NotRequired[
        "capo_kinesis.types.queue_starting_position.QueueStartingPosition"
    ]
    """<p>The position in the stream from which the queue begins delivering records. The default is <code>LATEST</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStreamConfiguration) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "starting_position" in value:
        import capo_kinesis.types.queue_starting_position

        out["StartingPosition"] = (
            capo_kinesis.types.queue_starting_position.serialize_aws_json_1_1(
                value["starting_position"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueStreamConfiguration:
    out: QueueStreamConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("StartingPosition") is not None:
        import capo_kinesis.types.queue_starting_position

        out["starting_position"] = (
            capo_kinesis.types.queue_starting_position.deserialize_aws_json_1_1(
                data["StartingPosition"]
            )
        )
    return out
