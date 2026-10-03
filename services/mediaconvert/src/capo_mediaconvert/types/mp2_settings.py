"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp2Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max2
    import capo_mediaconvert.types.__integer_min32000_max48000
    import capo_mediaconvert.types.__integer_min32000_max384000
    import capo_mediaconvert.types.mp2_audio_description_mix


class Mp2Settings(TypedDict, closed=True):
    audio_description_mix: NotRequired[
        "capo_mediaconvert.types.mp2_audio_description_mix.Mp2AudioDescriptionMix"
    ]
    """Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min32000_max384000.__integerMin32000Max384000"
    ]
    """Specify the average bitrate in bits per second."""
    channels: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2.__integerMin0Max2"
    ]
    """Set Channels to specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 0, 1, and 2."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min32000_max48000.__integerMin32000Max48000"
    ]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: Mp2Settings) -> dict:
    out: dict = {}
    if "audio_description_mix" in value:
        import capo_mediaconvert.types.mp2_audio_description_mix

        out["audioDescriptionMix"] = (
            capo_mediaconvert.types.mp2_audio_description_mix.serialize_json(
                value["audio_description_mix"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> Mp2Settings:
    out: Mp2Settings = {}  # type: ignore[typeddict-item]
    if data.get("audioDescriptionMix") is not None:
        import capo_mediaconvert.types.mp2_audio_description_mix

        out["audio_description_mix"] = (
            capo_mediaconvert.types.mp2_audio_description_mix.deserialize_json(
                data["audioDescriptionMix"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("channels") is not None:
        out["channels"] = data["channels"]
    if data.get("sampleRate") is not None:
        out["sample_rate"] = data["sampleRate"]
    return out
