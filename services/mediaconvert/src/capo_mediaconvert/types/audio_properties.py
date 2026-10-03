"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.__long
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.frame_rate


class AudioProperties(TypedDict, closed=True):
    bit_depth: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The bit depth of the audio track. This value is exact for PCM and FLAC audio. For lossy codecs, such as AAC, AC-3, and E-AC-3, it is a nominal value and should be treated as approximate."""
    bit_rate: NotRequired["capo_mediaconvert.types.__long.__long"]
    """The bit rate of the audio track, in bits per second."""
    channel_layout: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The audio channel layout of the track, such as "mono", "stereo", "5.1", or "7.1". Object-based or immersive audio is reported as "5.1.4" or "7.1.4". The layout is exact for AC-3 and E-AC-3 audio. For other codecs, it is inferred from the channel count and should be treated as approximate."""
    channels: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The number of audio channels in the audio track."""
    frame_rate: NotRequired["capo_mediaconvert.types.frame_rate.FrameRate"]
    """The frame rate of the video or audio track, expressed as a fraction with numerator and denominator values."""
    language_code: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The language code of the audio track, in three character ISO 639-3 format."""
    object_count: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The number of audio objects in an object-based or immersive audio track. This field is present for codecs that support object-based audio, such as E-AC-3 with Joint Object Coding (JOC) or IAMF. This field is null when the audio track does not contain object-based audio metadata."""
    sample_rate: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The sample rate of the audio track."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioProperties) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "bit_rate" in value:
        out["bitRate"] = value["bit_rate"]
    if "channel_layout" in value:
        out["channelLayout"] = value["channel_layout"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "frame_rate" in value:
        import capo_mediaconvert.types.frame_rate

        out["frameRate"] = capo_mediaconvert.types.frame_rate.serialize_json(
            value["frame_rate"]
        )
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "object_count" in value:
        out["objectCount"] = value["object_count"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> AudioProperties:
    out: AudioProperties = {}  # type: ignore[typeddict-item]
    if data.get("bitDepth") is not None:
        out["bit_depth"] = data["bitDepth"]
    if data.get("bitRate") is not None:
        out["bit_rate"] = data["bitRate"]
    if data.get("channelLayout") is not None:
        out["channel_layout"] = data["channelLayout"]
    if data.get("channels") is not None:
        out["channels"] = data["channels"]
    if data.get("frameRate") is not None:
        import capo_mediaconvert.types.frame_rate

        out["frame_rate"] = capo_mediaconvert.types.frame_rate.deserialize_json(
            data["frameRate"]
        )
    if data.get("languageCode") is not None:
        out["language_code"] = data["languageCode"]
    if data.get("objectCount") is not None:
        out["object_count"] = data["objectCount"]
    if data.get("sampleRate") is not None:
        out["sample_rate"] = data["sampleRate"]
    return out
