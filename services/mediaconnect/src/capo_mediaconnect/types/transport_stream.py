"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.color_information
    import capo_mediaconnect.types.frame_resolution
    import capo_mediaconnect.types.scan_mode


class TransportStream(TypedDict, closed=True):
    channels: NotRequired["int"]
    """<p> The number of channels in the audio stream.</p>"""
    codec: NotRequired["str"]
    """<p> The codec used by the stream.</p>"""
    color: NotRequired["capo_mediaconnect.types.color_information.ColorInformation"]
    """<p>The color signaling of the video stream.</p>"""
    frame_rate: NotRequired["str"]
    """<p> The frame rate used by the video stream.</p>"""
    frame_resolution: NotRequired[
        "capo_mediaconnect.types.frame_resolution.FrameResolution"
    ]
    """<p>The frame resolution used by the video stream. </p>"""
    pid: NotRequired["int"]
    """<p> The Packet ID (PID) as it is reported in the Program Map Table.</p>"""
    sample_rate: NotRequired["int"]
    """<p> The sample rate used by the audio stream.</p>"""
    sample_size: NotRequired["int"]
    """<p> The sample bit size used by the audio stream.</p>"""
    scan_mode: NotRequired["capo_mediaconnect.types.scan_mode.ScanMode"]
    """<p>The scan mode used by the video stream.</p>"""
    stream_type: NotRequired["str"]
    """<p> The Stream Type as it is reported in the Program Map Table.</p>"""
    language: NotRequired["str"]
    """<p>The language of the elementary stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransportStream) -> dict:
    out: dict = {}
    if "channels" in value:
        out["channels"] = value["channels"]
    if "codec" in value:
        out["codec"] = value["codec"]
    if "color" in value:
        import capo_mediaconnect.types.color_information

        out["color"] = capo_mediaconnect.types.color_information.serialize_json(
            value["color"]
        )
    if "frame_rate" in value:
        out["frameRate"] = value["frame_rate"]
    if "frame_resolution" in value:
        import capo_mediaconnect.types.frame_resolution

        out["frameResolution"] = (
            capo_mediaconnect.types.frame_resolution.serialize_json(
                value["frame_resolution"]
            )
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "sample_size" in value:
        out["sampleSize"] = value["sample_size"]
    if "scan_mode" in value:
        import capo_mediaconnect.types.scan_mode

        out["scanMode"] = capo_mediaconnect.types.scan_mode.serialize_json(
            value["scan_mode"]
        )
    if "stream_type" in value:
        out["streamType"] = value["stream_type"]
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_json(data: dict) -> TransportStream:
    out: TransportStream = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        out["channels"] = data["channels"]
    if data.get("codec") is not None:
        out["codec"] = data["codec"]
    if data.get("color") is not None:
        import capo_mediaconnect.types.color_information

        out["color"] = capo_mediaconnect.types.color_information.deserialize_json(
            data["color"]
        )
    if data.get("frameRate") is not None:
        out["frame_rate"] = data["frameRate"]
    if data.get("frameResolution") is not None:
        import capo_mediaconnect.types.frame_resolution

        out["frame_resolution"] = (
            capo_mediaconnect.types.frame_resolution.deserialize_json(
                data["frameResolution"]
            )
        )
    if data.get("pid") is not None:
        out["pid"] = data["pid"]
    if data.get("sampleRate") is not None:
        out["sample_rate"] = data["sampleRate"]
    if data.get("sampleSize") is not None:
        out["sample_size"] = data["sampleSize"]
    if data.get("scanMode") is not None:
        import capo_mediaconnect.types.scan_mode

        out["scan_mode"] = capo_mediaconnect.types.scan_mode.deserialize_json(
            data["scanMode"]
        )
    if data.get("streamType") is not None:
        out["stream_type"] = data["streamType"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    return out
