"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#JoinStorageSessionAsViewerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_webrtc_storage.types.channel_arn
    import capo_kinesis_video_webrtc_storage.types.client_id


class JoinStorageSessionAsViewerInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video_webrtc_storage.types.channel_arn.ChannelArn"
    """<p> The Amazon Resource Name (ARN) of the signaling channel. </p>"""
    client_id: "capo_kinesis_video_webrtc_storage.types.client_id.ClientId"
    """<p> The unique identifier for the sender client. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinStorageSessionAsViewerInput) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["clientId"] = value["client_id"]
    return out


def deserialize_json(data: dict) -> JoinStorageSessionAsViewerInput:
    out: JoinStorageSessionAsViewerInput = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    return out
