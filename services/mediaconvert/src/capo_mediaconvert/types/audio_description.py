"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max255
    import capo_mediaconvert.types.__string_max2048
    import capo_mediaconvert.types.__string_pattern_a_za_z23_a_za_z09
    import capo_mediaconvert.types.__string_pattern_ws
    import capo_mediaconvert.types.audio_channel_tagging_settings
    import capo_mediaconvert.types.audio_codec_settings
    import capo_mediaconvert.types.audio_language_code_control
    import capo_mediaconvert.types.audio_normalization_settings
    import capo_mediaconvert.types.audio_pitch_correction_settings
    import capo_mediaconvert.types.audio_type_control
    import capo_mediaconvert.types.language_code
    import capo_mediaconvert.types.remix_settings


class AudioDescription(TypedDict, closed=True):
    audio_channel_tagging_settings: NotRequired[
        "capo_mediaconvert.types.audio_channel_tagging_settings.AudioChannelTaggingSettings"
    ]
    """Specify the QuickTime audio channel layout tags for the audio channels in this audio track. When you don't specify a value, MediaConvert labels your track as Center (C) by default. To use Audio layout tagging, your output must be in a QuickTime (MOV) container and your audio codec must be AAC, WAV, or AIFF."""
    audio_normalization_settings: NotRequired[
        "capo_mediaconvert.types.audio_normalization_settings.AudioNormalizationSettings"
    ]
    """Advanced audio normalization settings. Ignore these settings unless you need to comply with a loudness standard."""
    audio_pitch_correction_settings: NotRequired[
        "capo_mediaconvert.types.audio_pitch_correction_settings.AudioPitchCorrectionSettings"
    ]
    """Settings for audio pitch correction during framerate conversion."""
    audio_source_name: NotRequired[
        "capo_mediaconvert.types.__string_max2048.__stringMax2048"
    ]
    """Specifies which audio data to use from each input. In the simplest case, specify an "Audio Selector":#inputs-audio_selector by name based on its order within each input. For example if you specify "Audio Selector 3", then the third audio selector will be used from each input. If an input does not have an "Audio Selector 3", then the audio selector marked as "default" in that input will be used. If there is no audio selector marked as "default", silence will be inserted for the duration of that input. Alternatively, an "Audio Selector Group":#inputs-audio_selector_group name may be specified, with similar default/silence behavior. If no audio_source_name is specified, then "Audio Selector 1" will be chosen automatically."""
    audio_type: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Applies only if Follow Input Audio Type is unchecked (false). A number between 0 and 255. The following are defined in ISO-IEC 13818-1: 0 = Undefined, 1 = Clean Effects, 2 = Hearing Impaired, 3 = Visually Impaired Commentary, 4-255 = Reserved."""
    audio_type_control: NotRequired[
        "capo_mediaconvert.types.audio_type_control.AudioTypeControl"
    ]
    """When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD."""
    codec_settings: NotRequired[
        "capo_mediaconvert.types.audio_codec_settings.AudioCodecSettings"
    ]
    """Settings related to audio encoding. The settings in this group vary depending on the value that you choose for your audio codec."""
    custom_language_code: NotRequired[
        "capo_mediaconvert.types.__string_pattern_a_za_z23_a_za_z09.__stringPatternAZaZ23AZaZ09"
    ]
    """Specify the language for this audio output track. The service puts this language code into your output audio track when you set Language code control to Use configured. The service also uses your specified custom language code when you set Language code control to Follow input, but your input file doesn't specify a language code. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming."""
    language_code: NotRequired["capo_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language for your output audio track. To follow the input language: Leave blank. When you do, also set Language code control to Follow input. If no input language is detected MediaConvert will not write an output language code. To follow the input langauge, but fall back to a specified language code if there is no input language to follow: Enter an ISO 639-2 three-letter language code in all capital letters. When you do, also set Language code control to Follow input. To specify the language code: Enter an ISO 639 three-letter language code in all capital letters. When you do, also set Language code control to Use configured."""
    language_code_control: NotRequired[
        "capo_mediaconvert.types.audio_language_code_control.AudioLanguageCodeControl"
    ]
    """Specify which source for language code takes precedence for this audio track. When you choose Follow input, the service uses the language code from the input track if it's present. If there's no languge code on the input track, the service uses the code that you specify in the setting Language code. When you choose Use configured, the service uses the language code that you specify."""
    remix_settings: NotRequired["capo_mediaconvert.types.remix_settings.RemixSettings"]
    """Advanced audio remixing settings."""
    stream_name: NotRequired[
        "capo_mediaconvert.types.__string_pattern_ws.__stringPatternWS"
    ]
    """Specify a label for this output audio stream. For example, "English", "Director commentary", or "track_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioDescription) -> dict:
    out: dict = {}
    if "audio_channel_tagging_settings" in value:
        import capo_mediaconvert.types.audio_channel_tagging_settings

        out["audioChannelTaggingSettings"] = (
            capo_mediaconvert.types.audio_channel_tagging_settings.serialize_json(
                value["audio_channel_tagging_settings"]
            )
        )
    if "audio_normalization_settings" in value:
        import capo_mediaconvert.types.audio_normalization_settings

        out["audioNormalizationSettings"] = (
            capo_mediaconvert.types.audio_normalization_settings.serialize_json(
                value["audio_normalization_settings"]
            )
        )
    if "audio_pitch_correction_settings" in value:
        import capo_mediaconvert.types.audio_pitch_correction_settings

        out["audioPitchCorrectionSettings"] = (
            capo_mediaconvert.types.audio_pitch_correction_settings.serialize_json(
                value["audio_pitch_correction_settings"]
            )
        )
    if "audio_source_name" in value:
        out["audioSourceName"] = value["audio_source_name"]
    if "audio_type" in value:
        out["audioType"] = value["audio_type"]
    if "audio_type_control" in value:
        import capo_mediaconvert.types.audio_type_control

        out["audioTypeControl"] = (
            capo_mediaconvert.types.audio_type_control.serialize_json(
                value["audio_type_control"]
            )
        )
    if "codec_settings" in value:
        import capo_mediaconvert.types.audio_codec_settings

        out["codecSettings"] = (
            capo_mediaconvert.types.audio_codec_settings.serialize_json(
                value["codec_settings"]
            )
        )
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "language_code" in value:
        import capo_mediaconvert.types.language_code

        out["languageCode"] = capo_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "language_code_control" in value:
        import capo_mediaconvert.types.audio_language_code_control

        out["languageCodeControl"] = (
            capo_mediaconvert.types.audio_language_code_control.serialize_json(
                value["language_code_control"]
            )
        )
    if "remix_settings" in value:
        import capo_mediaconvert.types.remix_settings

        out["remixSettings"] = capo_mediaconvert.types.remix_settings.serialize_json(
            value["remix_settings"]
        )
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    return out


def deserialize_json(data: dict) -> AudioDescription:
    out: AudioDescription = {}  # type: ignore[typeddict-item]
    if data.get("audioChannelTaggingSettings") is not None:
        import capo_mediaconvert.types.audio_channel_tagging_settings

        out["audio_channel_tagging_settings"] = (
            capo_mediaconvert.types.audio_channel_tagging_settings.deserialize_json(
                data["audioChannelTaggingSettings"]
            )
        )
    if data.get("audioNormalizationSettings") is not None:
        import capo_mediaconvert.types.audio_normalization_settings

        out["audio_normalization_settings"] = (
            capo_mediaconvert.types.audio_normalization_settings.deserialize_json(
                data["audioNormalizationSettings"]
            )
        )
    if data.get("audioPitchCorrectionSettings") is not None:
        import capo_mediaconvert.types.audio_pitch_correction_settings

        out["audio_pitch_correction_settings"] = (
            capo_mediaconvert.types.audio_pitch_correction_settings.deserialize_json(
                data["audioPitchCorrectionSettings"]
            )
        )
    if data.get("audioSourceName") is not None:
        out["audio_source_name"] = data["audioSourceName"]
    if data.get("audioType") is not None:
        out["audio_type"] = data["audioType"]
    if data.get("audioTypeControl") is not None:
        import capo_mediaconvert.types.audio_type_control

        out["audio_type_control"] = (
            capo_mediaconvert.types.audio_type_control.deserialize_json(
                data["audioTypeControl"]
            )
        )
    if data.get("codecSettings") is not None:
        import capo_mediaconvert.types.audio_codec_settings

        out["codec_settings"] = (
            capo_mediaconvert.types.audio_codec_settings.deserialize_json(
                data["codecSettings"]
            )
        )
    if data.get("customLanguageCode") is not None:
        out["custom_language_code"] = data["customLanguageCode"]
    if data.get("languageCode") is not None:
        import capo_mediaconvert.types.language_code

        out["language_code"] = capo_mediaconvert.types.language_code.deserialize_json(
            data["languageCode"]
        )
    if data.get("languageCodeControl") is not None:
        import capo_mediaconvert.types.audio_language_code_control

        out["language_code_control"] = (
            capo_mediaconvert.types.audio_language_code_control.deserialize_json(
                data["languageCodeControl"]
            )
        )
    if data.get("remixSettings") is not None:
        import capo_mediaconvert.types.remix_settings

        out["remix_settings"] = capo_mediaconvert.types.remix_settings.deserialize_json(
            data["remixSettings"]
        )
    if data.get("streamName") is not None:
        out["stream_name"] = data["streamName"]
    return out
