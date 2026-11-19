"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpMediaStreamInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.rtmp_media_stream_info

RtmpMediaStreamInfoList: TypeAlias = list[
    "capo_mediaconnect.types.rtmp_media_stream_info.RtmpMediaStreamInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RtmpMediaStreamInfoList) -> list:
    import capo_mediaconnect.types.rtmp_media_stream_info

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.rtmp_media_stream_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RtmpMediaStreamInfoList:
    import capo_mediaconnect.types.rtmp_media_stream_info

    out: RtmpMediaStreamInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.rtmp_media_stream_info.deserialize_json(item)
        )
    return out
