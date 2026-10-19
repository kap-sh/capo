"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelStreamDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.record_configuration
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.timestamp


class ChannelStreamDescription(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) of the source Kinesis data stream.</p>"""
    stream_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The time at which the source stream was created.</p>"""
    record_configuration: "capo_kinesis.types.record_configuration.RecordConfiguration"
    """<p>The record format configuration for the source stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelStreamDescription) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    import capo_kinesis.types.timestamp

    out["StreamCreationTimestamp"] = (
        capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["stream_creation_timestamp"]
        )
    )
    import capo_kinesis.types.record_configuration

    out["RecordConfiguration"] = (
        capo_kinesis.types.record_configuration.serialize_aws_json_1_1(
            value["record_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelStreamDescription:
    out: ChannelStreamDescription = {}  # type: ignore[typeddict-item]
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
    else:
        import datetime

        out["stream_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RecordConfiguration") is not None:
        import capo_kinesis.types.record_configuration

        out["record_configuration"] = (
            capo_kinesis.types.record_configuration.deserialize_aws_json_1_1(
                data["RecordConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelStreamDescription.record_configuration required"
        )
    return out
