"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min6_max16
    import capo_mediaconvert.types.__integer_min2000_max30000
    import capo_mediaconvert.types.__integer_min6000_max1024000
    import capo_mediaconvert.types.__integer_min8000_max96000
    import capo_mediaconvert.types.aac_audio_description_broadcaster_mix
    import capo_mediaconvert.types.aac_codec_profile
    import capo_mediaconvert.types.aac_coding_mode
    import capo_mediaconvert.types.aac_loudness_measurement_mode
    import capo_mediaconvert.types.aac_passthrough_control
    import capo_mediaconvert.types.aac_rate_control_mode
    import capo_mediaconvert.types.aac_raw_format
    import capo_mediaconvert.types.aac_specification
    import capo_mediaconvert.types.aac_vbr_quality


class AacSettings(TypedDict, closed=True):
    audio_description_broadcaster_mix: NotRequired[
        "capo_mediaconvert.types.aac_audio_description_broadcaster_mix.AacAudioDescriptionBroadcasterMix"
    ]
    """Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NORMAL when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min6000_max1024000.__integerMin6000Max1024000"
    ]
    """Specify the average bitrate in bits per second. The set of valid values for this setting is: 6000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000. The value you set is also constrained by the values that you choose for Profile, Bitrate control mode, and Sample rate. Default values depend on Bitrate control mode and Profile."""
    codec_profile: NotRequired[
        "capo_mediaconvert.types.aac_codec_profile.AacCodecProfile"
    ]
    """Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE."""
    coding_mode: NotRequired["capo_mediaconvert.types.aac_coding_mode.AacCodingMode"]
    """The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. * 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. * 1.0 Mono: One channel, C. * 2.0 Stereo: Two channels, L, R. * 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING_MODE_AUTO, and the service will automatically choose from one of the coding modes above."""
    loudness_measurement_mode: NotRequired[
        "capo_mediaconvert.types.aac_loudness_measurement_mode.AacLoudnessMeasurementMode"
    ]
    """Choose the loudness measurement mode for your audio content. For music or advertisements: We recommend that you keep the default value, Program. For speech or other content: We recommend that you choose Anchor. When you do, MediaConvert optimizes the loudness of your output for clarify by applying speech gates."""
    passthrough_control: NotRequired[
        "capo_mediaconvert.types.aac_passthrough_control.AacPassthroughControl"
    ]
    """When set to WHEN_POSSIBLE, input AAC audio will be passed through if it is present on the input. This detection is dynamic over the life of the transcode. Inputs that alternate between AAC and non-AAC content will have a consistent AAC output as the system alternates between passthrough and encoding."""
    rap_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min2000_max30000.__integerMin2000Max30000"
    ]
    """Specify the RAP (Random Access Point) interval for your xHE-AAC audio output. A RAP allows a decoder to decode audio data mid-stream, without the need to reference previous audio frames, and perform adaptive audio bitrate switching. To specify the RAP interval: Enter an integer from 2000 to 30000, in milliseconds. Smaller values allow for better seeking and more frequent stream switching, while large values improve compression efficiency. To have MediaConvert automatically determine the RAP interval: Leave blank."""
    rate_control_mode: NotRequired[
        "capo_mediaconvert.types.aac_rate_control_mode.AacRateControlMode"
    ]
    """Specify the AAC rate control mode. For a constant bitrate: Choose CBR. Your AAC output bitrate will be equal to the value that you choose for Bitrate. For a variable bitrate: Choose VBR. Your AAC output bitrate will vary according to your audio content and the value that you choose for Bitrate quality."""
    raw_format: NotRequired["capo_mediaconvert.types.aac_raw_format.AacRawFormat"]
    """Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min8000_max96000.__integerMin8000Max96000"
    ]
    """Specify the AAC sample rate in samples per second (Hz). Valid sample rates depend on the AAC profile and Coding mode that you select. For a list of supported sample rates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html"""
    specification: NotRequired[
        "capo_mediaconvert.types.aac_specification.AacSpecification"
    ]
    """Use MPEG-2 AAC instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers."""
    target_loudness_range: NotRequired[
        "capo_mediaconvert.types.__integer_min6_max16.__integerMin6Max16"
    ]
    """Specify the xHE-AAC loudness target. Enter an integer from 6 to 16, representing "loudness units". For more information, see the following specification: Supplementary information for R 128 EBU Tech 3342-2023."""
    vbr_quality: NotRequired["capo_mediaconvert.types.aac_vbr_quality.AacVbrQuality"]
    """Specify the quality of your variable bitrate (VBR) AAC audio. For a list of approximate VBR bitrates, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/aac-support.html#aac_vbr"""


# --- restJson1 ser/de ---
def serialize_json(value: AacSettings) -> dict:
    out: dict = {}
    if "audio_description_broadcaster_mix" in value:
        import capo_mediaconvert.types.aac_audio_description_broadcaster_mix

        out["audioDescriptionBroadcasterMix"] = (
            capo_mediaconvert.types.aac_audio_description_broadcaster_mix.serialize_json(
                value["audio_description_broadcaster_mix"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "codec_profile" in value:
        import capo_mediaconvert.types.aac_codec_profile

        out["codecProfile"] = capo_mediaconvert.types.aac_codec_profile.serialize_json(
            value["codec_profile"]
        )
    if "coding_mode" in value:
        import capo_mediaconvert.types.aac_coding_mode

        out["codingMode"] = capo_mediaconvert.types.aac_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "loudness_measurement_mode" in value:
        import capo_mediaconvert.types.aac_loudness_measurement_mode

        out["loudnessMeasurementMode"] = (
            capo_mediaconvert.types.aac_loudness_measurement_mode.serialize_json(
                value["loudness_measurement_mode"]
            )
        )
    if "passthrough_control" in value:
        import capo_mediaconvert.types.aac_passthrough_control

        out["passthroughControl"] = (
            capo_mediaconvert.types.aac_passthrough_control.serialize_json(
                value["passthrough_control"]
            )
        )
    if "rap_interval" in value:
        out["rapInterval"] = value["rap_interval"]
    if "rate_control_mode" in value:
        import capo_mediaconvert.types.aac_rate_control_mode

        out["rateControlMode"] = (
            capo_mediaconvert.types.aac_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "raw_format" in value:
        import capo_mediaconvert.types.aac_raw_format

        out["rawFormat"] = capo_mediaconvert.types.aac_raw_format.serialize_json(
            value["raw_format"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "specification" in value:
        import capo_mediaconvert.types.aac_specification

        out["specification"] = capo_mediaconvert.types.aac_specification.serialize_json(
            value["specification"]
        )
    if "target_loudness_range" in value:
        out["targetLoudnessRange"] = value["target_loudness_range"]
    if "vbr_quality" in value:
        import capo_mediaconvert.types.aac_vbr_quality

        out["vbrQuality"] = capo_mediaconvert.types.aac_vbr_quality.serialize_json(
            value["vbr_quality"]
        )
    return out


def deserialize_json(data: dict) -> AacSettings:
    out: AacSettings = {}  # type: ignore[typeddict-item]
    if data.get("audioDescriptionBroadcasterMix") is not None:
        import capo_mediaconvert.types.aac_audio_description_broadcaster_mix

        out["audio_description_broadcaster_mix"] = (
            capo_mediaconvert.types.aac_audio_description_broadcaster_mix.deserialize_json(
                data["audioDescriptionBroadcasterMix"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("codecProfile") is not None:
        import capo_mediaconvert.types.aac_codec_profile

        out["codec_profile"] = (
            capo_mediaconvert.types.aac_codec_profile.deserialize_json(
                data["codecProfile"]
            )
        )
    if data.get("codingMode") is not None:
        import capo_mediaconvert.types.aac_coding_mode

        out["coding_mode"] = capo_mediaconvert.types.aac_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if data.get("loudnessMeasurementMode") is not None:
        import capo_mediaconvert.types.aac_loudness_measurement_mode

        out["loudness_measurement_mode"] = (
            capo_mediaconvert.types.aac_loudness_measurement_mode.deserialize_json(
                data["loudnessMeasurementMode"]
            )
        )
    if data.get("passthroughControl") is not None:
        import capo_mediaconvert.types.aac_passthrough_control

        out["passthrough_control"] = (
            capo_mediaconvert.types.aac_passthrough_control.deserialize_json(
                data["passthroughControl"]
            )
        )
    if data.get("rapInterval") is not None:
        out["rap_interval"] = data["rapInterval"]
    if data.get("rateControlMode") is not None:
        import capo_mediaconvert.types.aac_rate_control_mode

        out["rate_control_mode"] = (
            capo_mediaconvert.types.aac_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("rawFormat") is not None:
        import capo_mediaconvert.types.aac_raw_format

        out["raw_format"] = capo_mediaconvert.types.aac_raw_format.deserialize_json(
            data["rawFormat"]
        )
    if data.get("sampleRate") is not None:
        out["sample_rate"] = data["sampleRate"]
    if data.get("specification") is not None:
        import capo_mediaconvert.types.aac_specification

        out["specification"] = (
            capo_mediaconvert.types.aac_specification.deserialize_json(
                data["specification"]
            )
        )
    if data.get("targetLoudnessRange") is not None:
        out["target_loudness_range"] = data["targetLoudnessRange"]
    if data.get("vbrQuality") is not None:
        import capo_mediaconvert.types.aac_vbr_quality

        out["vbr_quality"] = capo_mediaconvert.types.aac_vbr_quality.deserialize_json(
            data["vbrQuality"]
        )
    return out
