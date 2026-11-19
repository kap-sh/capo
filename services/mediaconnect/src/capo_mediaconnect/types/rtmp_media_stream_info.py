"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpMediaStreamInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.color_information
    import capo_mediaconnect.types.frame_resolution
    import capo_mediaconnect.types.scan_mode
    import capo_mediaconnect.types.source_media_stream_type


class RtmpMediaStreamInfo(TypedDict, closed=True):
    stream_id: NotRequired["int"]
    """<p>A unique identifier for the stream.</p>"""
    stream_type: NotRequired[
        "capo_mediaconnect.types.source_media_stream_type.SourceMediaStreamType"
    ]
    """<p>The type of stream (for example, <code>VIDEO</code> or <code>AUDIO</code>).</p>"""
    codec: NotRequired["str"]
    """<p>The codec used for the stream.</p>"""
    frame_rate: NotRequired["str"]
    """<p>The number of video frames displayed per second. Used when the <code>streamType</code> is <code>VIDEO</code>.</p>"""
    frame_resolution: NotRequired[
        "capo_mediaconnect.types.frame_resolution.FrameResolution"
    ]
    """<p>The width and height dimensions of the video frame in pixels. Used when the <code>streamType</code> is <code>VIDEO</code>.</p>"""
    scan_mode: NotRequired["capo_mediaconnect.types.scan_mode.ScanMode"]
    """<p>The method used to display video frames. Used when the <code>streamType</code> is <code>VIDEO</code>.</p>"""
    color: NotRequired["capo_mediaconnect.types.color_information.ColorInformation"]
    """<p>The color signaling of the video stream. Used when the <code>streamType</code> is <code>VIDEO</code>.</p>"""
    channels: NotRequired["int"]
    """<p>The number of audio channels in the stream. Used when the <code>streamType</code> is <code>AUDIO</code>.</p>"""
    sample_rate: NotRequired["int"]
    """<p>The number of audio samples captured per second. Used when the <code>streamType</code> is <code>AUDIO</code>.</p>"""
    sample_size: NotRequired["int"]
    """<p>The sample bit size used by the audio stream. Used when the <code>streamType</code> is <code>AUDIO</code>.</p>"""
    language: NotRequired["str"]
    """<p>The language of the audio stream. Used when the <code>streamType</code> is <code>AUDIO</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpMediaStreamInfo) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "stream_type" in value:
        import capo_mediaconnect.types.source_media_stream_type

        out["streamType"] = (
            capo_mediaconnect.types.source_media_stream_type.serialize_json(
                value["stream_type"]
            )
        )
    if "codec" in value:
        out["codec"] = value["codec"]
    if "frame_rate" in value:
        out["frameRate"] = value["frame_rate"]
    if "frame_resolution" in value:
        import capo_mediaconnect.types.frame_resolution

        out["frameResolution"] = (
            capo_mediaconnect.types.frame_resolution.serialize_json(
                value["frame_resolution"]
            )
        )
    if "scan_mode" in value:
        import capo_mediaconnect.types.scan_mode

        out["scanMode"] = capo_mediaconnect.types.scan_mode.serialize_json(
            value["scan_mode"]
        )
    if "color" in value:
        import capo_mediaconnect.types.color_information

        out["color"] = capo_mediaconnect.types.color_information.serialize_json(
            value["color"]
        )
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "sample_size" in value:
        out["sampleSize"] = value["sample_size"]
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_json(data: dict) -> RtmpMediaStreamInfo:
    out: RtmpMediaStreamInfo = {}  # type: ignore[typeddict-item]
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("streamType") is not None:
        import capo_mediaconnect.types.source_media_stream_type

        out["stream_type"] = (
            capo_mediaconnect.types.source_media_stream_type.deserialize_json(
                data["streamType"]
            )
        )
    if data.get("codec") is not None:
        out["codec"] = data["codec"]
    if data.get("frameRate") is not None:
        out["frame_rate"] = data["frameRate"]
    if data.get("frameResolution") is not None:
        import capo_mediaconnect.types.frame_resolution

        out["frame_resolution"] = (
            capo_mediaconnect.types.frame_resolution.deserialize_json(
                data["frameResolution"]
            )
        )
    if data.get("scanMode") is not None:
        import capo_mediaconnect.types.scan_mode

        out["scan_mode"] = capo_mediaconnect.types.scan_mode.deserialize_json(
            data["scanMode"]
        )
    if data.get("color") is not None:
        import capo_mediaconnect.types.color_information

        out["color"] = capo_mediaconnect.types.color_information.deserialize_json(
            data["color"]
        )
    if data.get("channels") is not None:
        out["channels"] = data["channels"]
    if data.get("sampleRate") is not None:
        out["sample_rate"] = data["sampleRate"]
    if data.get("sampleSize") is not None:
        out["sample_size"] = data["sampleSize"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    return out
