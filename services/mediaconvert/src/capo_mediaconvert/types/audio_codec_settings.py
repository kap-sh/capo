"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioCodecSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.aac_settings
    import capo_mediaconvert.types.ac3_settings
    import capo_mediaconvert.types.ac4_settings
    import capo_mediaconvert.types.aiff_settings
    import capo_mediaconvert.types.audio_codec
    import capo_mediaconvert.types.eac3_atmos_settings
    import capo_mediaconvert.types.eac3_settings
    import capo_mediaconvert.types.flac_settings
    import capo_mediaconvert.types.mp2_settings
    import capo_mediaconvert.types.mp3_settings
    import capo_mediaconvert.types.opus_settings
    import capo_mediaconvert.types.vorbis_settings
    import capo_mediaconvert.types.wav_settings


class AudioCodecSettings(TypedDict, closed=True):
    aac_settings: NotRequired["capo_mediaconvert.types.aac_settings.AacSettings"]
    """Required when you set Codec to the value AAC. The service accepts one of two mutually exclusive groups of AAC settings--VBR and CBR. To select one of these modes, set the value of Bitrate control mode to "VBR" or "CBR". In VBR mode, you control the audio quality with the setting VBR quality. In CBR mode, you use the setting Bitrate. Defaults and valid values depend on the rate control mode."""
    ac3_settings: NotRequired["capo_mediaconvert.types.ac3_settings.Ac3Settings"]
    """Required when you set Codec to the value AC3."""
    ac4_settings: NotRequired["capo_mediaconvert.types.ac4_settings.Ac4Settings"]
    """Required when you set Codec to the value AC4."""
    aiff_settings: NotRequired["capo_mediaconvert.types.aiff_settings.AiffSettings"]
    """Required when you set Codec to the value AIFF."""
    codec: NotRequired["capo_mediaconvert.types.audio_codec.AudioCodec"]
    """Choose the audio codec for this output. Note that the option passthrough applies only to Dolby Digital, Dolby Digital Plus, AAC LC, AAC HEV1, and AAC HEV2 audio inputs. Make sure that you choose a codec that's supported with your output container: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#reference-codecs-containers-output-audio For audio-only outputs, make sure that both your input audio codec and your output audio codec are supported for audio-only workflows. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-audio-only and https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers.html#audio-only-output"""
    eac3_atmos_settings: NotRequired[
        "capo_mediaconvert.types.eac3_atmos_settings.Eac3AtmosSettings"
    ]
    """Required when you set Codec to the value EAC3_ATMOS."""
    eac3_settings: NotRequired["capo_mediaconvert.types.eac3_settings.Eac3Settings"]
    """Required when you set Codec to the value EAC3."""
    flac_settings: NotRequired["capo_mediaconvert.types.flac_settings.FlacSettings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value FLAC."""
    mp2_settings: NotRequired["capo_mediaconvert.types.mp2_settings.Mp2Settings"]
    """Required when you set Codec to the value MP2."""
    mp3_settings: NotRequired["capo_mediaconvert.types.mp3_settings.Mp3Settings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value MP3."""
    opus_settings: NotRequired["capo_mediaconvert.types.opus_settings.OpusSettings"]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value OPUS."""
    vorbis_settings: NotRequired[
        "capo_mediaconvert.types.vorbis_settings.VorbisSettings"
    ]
    """Required when you set Codec, under AudioDescriptions>CodecSettings, to the value Vorbis."""
    wav_settings: NotRequired["capo_mediaconvert.types.wav_settings.WavSettings"]
    """Required when you set Codec to the value WAV."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioCodecSettings) -> dict:
    out: dict = {}
    if "aac_settings" in value:
        import capo_mediaconvert.types.aac_settings

        out["aacSettings"] = capo_mediaconvert.types.aac_settings.serialize_json(
            value["aac_settings"]
        )
    if "ac3_settings" in value:
        import capo_mediaconvert.types.ac3_settings

        out["ac3Settings"] = capo_mediaconvert.types.ac3_settings.serialize_json(
            value["ac3_settings"]
        )
    if "ac4_settings" in value:
        import capo_mediaconvert.types.ac4_settings

        out["ac4Settings"] = capo_mediaconvert.types.ac4_settings.serialize_json(
            value["ac4_settings"]
        )
    if "aiff_settings" in value:
        import capo_mediaconvert.types.aiff_settings

        out["aiffSettings"] = capo_mediaconvert.types.aiff_settings.serialize_json(
            value["aiff_settings"]
        )
    if "codec" in value:
        import capo_mediaconvert.types.audio_codec

        out["codec"] = capo_mediaconvert.types.audio_codec.serialize_json(
            value["codec"]
        )
    if "eac3_atmos_settings" in value:
        import capo_mediaconvert.types.eac3_atmos_settings

        out["eac3AtmosSettings"] = (
            capo_mediaconvert.types.eac3_atmos_settings.serialize_json(
                value["eac3_atmos_settings"]
            )
        )
    if "eac3_settings" in value:
        import capo_mediaconvert.types.eac3_settings

        out["eac3Settings"] = capo_mediaconvert.types.eac3_settings.serialize_json(
            value["eac3_settings"]
        )
    if "flac_settings" in value:
        import capo_mediaconvert.types.flac_settings

        out["flacSettings"] = capo_mediaconvert.types.flac_settings.serialize_json(
            value["flac_settings"]
        )
    if "mp2_settings" in value:
        import capo_mediaconvert.types.mp2_settings

        out["mp2Settings"] = capo_mediaconvert.types.mp2_settings.serialize_json(
            value["mp2_settings"]
        )
    if "mp3_settings" in value:
        import capo_mediaconvert.types.mp3_settings

        out["mp3Settings"] = capo_mediaconvert.types.mp3_settings.serialize_json(
            value["mp3_settings"]
        )
    if "opus_settings" in value:
        import capo_mediaconvert.types.opus_settings

        out["opusSettings"] = capo_mediaconvert.types.opus_settings.serialize_json(
            value["opus_settings"]
        )
    if "vorbis_settings" in value:
        import capo_mediaconvert.types.vorbis_settings

        out["vorbisSettings"] = capo_mediaconvert.types.vorbis_settings.serialize_json(
            value["vorbis_settings"]
        )
    if "wav_settings" in value:
        import capo_mediaconvert.types.wav_settings

        out["wavSettings"] = capo_mediaconvert.types.wav_settings.serialize_json(
            value["wav_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioCodecSettings:
    out: AudioCodecSettings = {}  # type: ignore[typeddict-item]
    if data.get("aacSettings") is not None:
        import capo_mediaconvert.types.aac_settings

        out["aac_settings"] = capo_mediaconvert.types.aac_settings.deserialize_json(
            data["aacSettings"]
        )
    if data.get("ac3Settings") is not None:
        import capo_mediaconvert.types.ac3_settings

        out["ac3_settings"] = capo_mediaconvert.types.ac3_settings.deserialize_json(
            data["ac3Settings"]
        )
    if data.get("ac4Settings") is not None:
        import capo_mediaconvert.types.ac4_settings

        out["ac4_settings"] = capo_mediaconvert.types.ac4_settings.deserialize_json(
            data["ac4Settings"]
        )
    if data.get("aiffSettings") is not None:
        import capo_mediaconvert.types.aiff_settings

        out["aiff_settings"] = capo_mediaconvert.types.aiff_settings.deserialize_json(
            data["aiffSettings"]
        )
    if data.get("codec") is not None:
        import capo_mediaconvert.types.audio_codec

        out["codec"] = capo_mediaconvert.types.audio_codec.deserialize_json(
            data["codec"]
        )
    if data.get("eac3AtmosSettings") is not None:
        import capo_mediaconvert.types.eac3_atmos_settings

        out["eac3_atmos_settings"] = (
            capo_mediaconvert.types.eac3_atmos_settings.deserialize_json(
                data["eac3AtmosSettings"]
            )
        )
    if data.get("eac3Settings") is not None:
        import capo_mediaconvert.types.eac3_settings

        out["eac3_settings"] = capo_mediaconvert.types.eac3_settings.deserialize_json(
            data["eac3Settings"]
        )
    if data.get("flacSettings") is not None:
        import capo_mediaconvert.types.flac_settings

        out["flac_settings"] = capo_mediaconvert.types.flac_settings.deserialize_json(
            data["flacSettings"]
        )
    if data.get("mp2Settings") is not None:
        import capo_mediaconvert.types.mp2_settings

        out["mp2_settings"] = capo_mediaconvert.types.mp2_settings.deserialize_json(
            data["mp2Settings"]
        )
    if data.get("mp3Settings") is not None:
        import capo_mediaconvert.types.mp3_settings

        out["mp3_settings"] = capo_mediaconvert.types.mp3_settings.deserialize_json(
            data["mp3Settings"]
        )
    if data.get("opusSettings") is not None:
        import capo_mediaconvert.types.opus_settings

        out["opus_settings"] = capo_mediaconvert.types.opus_settings.deserialize_json(
            data["opusSettings"]
        )
    if data.get("vorbisSettings") is not None:
        import capo_mediaconvert.types.vorbis_settings

        out["vorbis_settings"] = (
            capo_mediaconvert.types.vorbis_settings.deserialize_json(
                data["vorbisSettings"]
            )
        )
    if data.get("wavSettings") is not None:
        import capo_mediaconvert.types.wav_settings

        out["wav_settings"] = capo_mediaconvert.types.wav_settings.deserialize_json(
            data["wavSettings"]
        )
    return out
