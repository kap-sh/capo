"""Generated from Smithy shape ``com.amazonaws.kinesis#ChannelStreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.record_configuration
    import capo_kinesis.types.stream_arn


class ChannelStreamConfiguration(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The Amazon Resource Name (ARN) of the source Kinesis data stream.</p>"""
    record_configuration: "capo_kinesis.types.record_configuration.RecordConfiguration"
    """<p>The record format configuration for the source stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelStreamConfiguration) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    import capo_kinesis.types.record_configuration

    out["RecordConfiguration"] = (
        capo_kinesis.types.record_configuration.serialize_aws_json_1_1(
            value["record_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelStreamConfiguration:
    out: ChannelStreamConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        out["stream_arn"] = ""
    if data.get("RecordConfiguration") is not None:
        import capo_kinesis.types.record_configuration

        out["record_configuration"] = (
            capo_kinesis.types.record_configuration.deserialize_aws_json_1_1(
                data["RecordConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ChannelStreamConfiguration.record_configuration required"
        )
    return out
