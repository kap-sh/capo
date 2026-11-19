"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpSourceMetadataInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_media_info


class RtmpSourceMetadataInfo(TypedDict, closed=True):
    application_name: NotRequired["str"]
    """<p>The name of the RTMP application.</p>"""
    stream_name: NotRequired["str"]
    """<p>The name of the RTMP stream.</p>"""
    media_info: NotRequired["capo_mediaconnect.types.rtmp_media_info.RtmpMediaInfo"]
    """<p>Information about the audio and video streams that are part of the RTMP source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpSourceMetadataInfo) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "media_info" in value:
        import capo_mediaconnect.types.rtmp_media_info

        out["mediaInfo"] = capo_mediaconnect.types.rtmp_media_info.serialize_json(
            value["media_info"]
        )
    return out


def deserialize_json(data: dict) -> RtmpSourceMetadataInfo:
    out: RtmpSourceMetadataInfo = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    if data.get("mediaInfo") is not None:
        import capo_mediaconnect.types.rtmp_media_info

        out["media_info"] = capo_mediaconnect.types.rtmp_media_info.deserialize_json(
            data["mediaInfo"]
        )
    return out
