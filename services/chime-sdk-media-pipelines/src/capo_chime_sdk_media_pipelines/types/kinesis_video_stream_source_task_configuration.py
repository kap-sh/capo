"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamSourceTaskConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.channel_id
    import capo_chime_sdk_media_pipelines.types.fragment_number_string
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_arn


class KinesisVideoStreamSourceTaskConfiguration(TypedDict, closed=True):
    stream_arn: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_arn.KinesisVideoStreamArn"
    """<p>The ARN of the stream.</p>"""
    channel_id: "capo_chime_sdk_media_pipelines.types.channel_id.ChannelId"
    """<p>The channel ID.</p>"""
    fragment_number: NotRequired[
        "capo_chime_sdk_media_pipelines.types.fragment_number_string.FragmentNumberString"
    ]
    """<p>The unique identifier of the fragment to begin processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamSourceTaskConfiguration) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    out["ChannelId"] = value.get("channel_id", 0)
    if "fragment_number" in value:
        out["FragmentNumber"] = value["fragment_number"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamSourceTaskConfiguration:
    out: KinesisVideoStreamSourceTaskConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("ChannelId") is not None:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if data.get("FragmentNumber") is not None:
        out["fragment_number"] = data["FragmentNumber"]
    return out
