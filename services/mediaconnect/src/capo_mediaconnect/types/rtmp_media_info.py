"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpMediaInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_media_stream_info_list


class RtmpMediaInfo(TypedDict, closed=True):
    streams: NotRequired[
        "capo_mediaconnect.types.rtmp_media_stream_info_list.RtmpMediaStreamInfoList"
    ]
    """<p>A list of the individual audio and video streams that make up the RTMP source. This includes details about each stream's codec, resolution, frame rate, audio channels, and other parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpMediaInfo) -> dict:
    out: dict = {}
    if "streams" in value:
        import capo_mediaconnect.types.rtmp_media_stream_info_list

        out["streams"] = (
            capo_mediaconnect.types.rtmp_media_stream_info_list.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtmpMediaInfo:
    out: RtmpMediaInfo = {}  # type: ignore[typeddict-item]
    if data.get("streams") is not None:
        import capo_mediaconnect.types.rtmp_media_stream_info_list

        out["streams"] = (
            capo_mediaconnect.types.rtmp_media_stream_info_list.deserialize_json(
                data["streams"]
            )
        )
    return out
