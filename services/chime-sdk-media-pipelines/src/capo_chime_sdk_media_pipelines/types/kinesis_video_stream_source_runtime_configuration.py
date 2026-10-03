"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamSourceRuntimeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_encoding
    import capo_chime_sdk_media_pipelines.types.media_sample_rate_hertz
    import capo_chime_sdk_media_pipelines.types.streams


class KinesisVideoStreamSourceRuntimeConfiguration(TypedDict, closed=True):
    streams: "capo_chime_sdk_media_pipelines.types.streams.Streams"
    """<p>The streams in the source runtime configuration of a Kinesis video stream.</p>"""
    media_encoding: "capo_chime_sdk_media_pipelines.types.media_encoding.MediaEncoding"
    """<p>Specifies the encoding of your input audio. Supported format: PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    media_sample_rate: "capo_chime_sdk_media_pipelines.types.media_sample_rate_hertz.MediaSampleRateHertz"
    """<p>The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p> <p>Valid Range: Minimum value of 8000. Maximum value of 48000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamSourceRuntimeConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.streams

    out["Streams"] = capo_chime_sdk_media_pipelines.types.streams.serialize_json(
        value["streams"]
    )
    import capo_chime_sdk_media_pipelines.types.media_encoding

    out["MediaEncoding"] = (
        capo_chime_sdk_media_pipelines.types.media_encoding.serialize_json(
            value["media_encoding"]
        )
    )
    out["MediaSampleRate"] = value["media_sample_rate"]
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamSourceRuntimeConfiguration:
    out: KinesisVideoStreamSourceRuntimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Streams") is not None:
        import capo_chime_sdk_media_pipelines.types.streams

        out["streams"] = capo_chime_sdk_media_pipelines.types.streams.deserialize_json(
            data["Streams"]
        )
    else:
        raise DeserializationError(
            "KinesisVideoStreamSourceRuntimeConfiguration.streams required"
        )
    if data.get("MediaEncoding") is not None:
        import capo_chime_sdk_media_pipelines.types.media_encoding

        out["media_encoding"] = (
            capo_chime_sdk_media_pipelines.types.media_encoding.deserialize_json(
                data["MediaEncoding"]
            )
        )
    else:
        raise DeserializationError(
            "KinesisVideoStreamSourceRuntimeConfiguration.media_encoding required"
        )
    if data.get("MediaSampleRate") is not None:
        out["media_sample_rate"] = data["MediaSampleRate"]
    else:
        raise DeserializationError(
            "KinesisVideoStreamSourceRuntimeConfiguration.media_sample_rate required"
        )
    return out
