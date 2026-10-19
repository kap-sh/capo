"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#StreamConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.fragment_number_string
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_arn
    import capo_chime_sdk_media_pipelines.types.stream_channel_definition


class StreamConfiguration(TypedDict, closed=True):
    stream_arn: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_arn.KinesisVideoStreamArn"
    """<p>The ARN of the stream.</p>"""
    fragment_number: NotRequired[
        "capo_chime_sdk_media_pipelines.types.fragment_number_string.FragmentNumberString"
    ]
    """<p>The unique identifier of the fragment to begin processing.</p>"""
    stream_channel_definition: "capo_chime_sdk_media_pipelines.types.stream_channel_definition.StreamChannelDefinition"
    """<p>The streaming channel definition in the stream configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamConfiguration) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    if "fragment_number" in value:
        out["FragmentNumber"] = value["fragment_number"]
    import capo_chime_sdk_media_pipelines.types.stream_channel_definition

    out["StreamChannelDefinition"] = (
        capo_chime_sdk_media_pipelines.types.stream_channel_definition.serialize_json(
            value["stream_channel_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> StreamConfiguration:
    out: StreamConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("FragmentNumber") is not None:
        out["fragment_number"] = data["FragmentNumber"]
    if data.get("StreamChannelDefinition") is not None:
        import capo_chime_sdk_media_pipelines.types.stream_channel_definition

        out["stream_channel_definition"] = (
            capo_chime_sdk_media_pipelines.types.stream_channel_definition.deserialize_json(
                data["StreamChannelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "StreamConfiguration.stream_channel_definition required"
        )
    return out
