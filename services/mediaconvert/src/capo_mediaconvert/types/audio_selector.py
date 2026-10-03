"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max8
    import capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import capo_mediaconvert.types.__list_of__integer_min1_max2147483647
    import capo_mediaconvert.types.__string_min3_max3_pattern_a_za_z3
    import capo_mediaconvert.types.__string_pattern_s3_https
    import capo_mediaconvert.types.audio_default_selection
    import capo_mediaconvert.types.audio_duration_correction
    import capo_mediaconvert.types.audio_selector_type
    import capo_mediaconvert.types.audio_smpte337_passthrough
    import capo_mediaconvert.types.hls_rendition_group_settings
    import capo_mediaconvert.types.language_code
    import capo_mediaconvert.types.remix_settings


class AudioSelector(TypedDict, closed=True):
    audio_duration_correction: NotRequired[
        "capo_mediaconvert.types.audio_duration_correction.AudioDurationCorrection"
    ]
    """Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: * Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. * Audio track: AAC. Choose from the following audio timing correction settings: * Disabled (Default): Apply no correction. * Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. * Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. * Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. * Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your input's STTS table. Your output audio and video may not be aligned or it may contain audio artifacts."""
    custom_language_code: NotRequired[
        "capo_mediaconvert.types.__string_min3_max3_pattern_a_za_z3.__stringMin3Max3PatternAZaZ3"
    ]
    """Selects a specific language code from within an audio source, using the ISO 639-2 or ISO 639-3 three-letter language code"""
    default_selection: NotRequired[
        "capo_mediaconvert.types.audio_default_selection.AudioDefaultSelection"
    ]
    """Specify a fallback audio selector for this input. Use to ensure outputs have audio even when the audio selector you specify in your output is missing from the source. DEFAULT (Checked in the MediaConvert console): If your output settings specify an audio selector that does not exist in this input, MediaConvert uses this audio selector instead. This is useful when you have multiple inputs with a different number of audio tracks. NOT_DEFAULT (Unchecked in the MediaConvert console): MediaConvert will not fallback from any missing audio selector. Any output specifying a missing audio selector will be silent."""
    external_audio_file_input: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_https.__stringPatternS3Https"
    ]
    """Specify the S3, HTTP, or HTTPS URL for your external audio file input."""
    hls_rendition_group_settings: NotRequired[
        "capo_mediaconvert.types.hls_rendition_group_settings.HlsRenditionGroupSettings"
    ]
    """Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead."""
    language_code: NotRequired["capo_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code_list.php"""
    offset: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647"""
    pids: NotRequired[
        "capo_mediaconvert.types.__list_of__integer_min1_max2147483647.__listOf__integerMin1Max2147483647"
    ]
    """Selects a specific PID from within an audio source (e.g. 257 selects PID 0x101)."""
    program_selection: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max8.__integerMin0Max8"
    ]
    """Use this setting for input streams that contain Dolby E, to have the service extract specific program data from the track. To select multiple programs, create multiple selectors with the same Track and different Program numbers. In the console, this setting is visible when you set Selector type to Track. Choose the program number from the dropdown list. If your input file has incorrect metadata, you can choose All channels instead of a program number to have the service ignore the program IDs and include all the programs in the track."""
    remix_settings: NotRequired["capo_mediaconvert.types.remix_settings.RemixSettings"]
    """Use these settings to reorder the audio channels of one input to match those of another input. This allows you to combine the two files into a single output, one after the other."""
    selector_type: NotRequired[
        "capo_mediaconvert.types.audio_selector_type.AudioSelectorType"
    ]
    """Specify how MediaConvert selects audio content within your input. The default is Track. PID: Select audio by specifying the Packet Identifier (PID) values for MPEG Transport Stream inputs. Use this when you know the exact PID values of your audio streams. Track: Default. Select audio by track number. This is the most common option and works with most input container formats. If more types of audio data get recognized in the future, these numberings may shift, but the numberings used for Stream mode will not. Language code: Select audio by language using an ISO 639-2 or ISO 639-3 three-letter code in all capital letters. Use this when your source has embedded language metadata and you want to select tracks based on their language. HLS rendition group: Select audio from an HLS rendition group. Use this when your input is an HLS package with multiple audio renditions and you want to select specific rendition groups. All PCM: Select all uncompressed PCM audio tracks from your input automatically. This is useful when you want to include all PCM audio tracks without specifying individual track numbers. Stream: Select audio by stream number. Stream numbers include all tracks in the source file, regardless of type, and correspond to either the order of tracks in the file, or if applicable, the stream number metadata of the track. Although all tracks count toward these stream numbers, in this audio selector context, only the stream number of a track containing audio data may be used. If your source file contains a track which is not recognized by the service, then the corresponding stream number will still be reserved for future use. If more types of audio data get recognized in the future, these numberings will not shift."""
    smpte337_passthrough: NotRequired[
        "capo_mediaconvert.types.audio_smpte337_passthrough.AudioSmpte337Passthrough"
    ]
    """Specify whether to pass SMPTE 337M-wrapped audio (such as Dolby E) through without unwrapping. Choose Enabled to pass the SMPTE 337M container through unchanged, treating the track as raw PCM. Choose Disabled (default) to automatically detect and unwrap SMPTE 337M data, extracting the underlying Dolby E programs as separate audio tracks for encoding. When this field is absent, the service defaults to Disabled (auto-unwrap)."""
    streams: NotRequired[
        "capo_mediaconvert.types.__list_of__integer_min1_max2147483647.__listOf__integerMin1Max2147483647"
    ]
    """Identify a track from the input audio to include in this selector by entering the stream index number. These numberings count all tracks in the input file, but only a track containing audio data may be used here. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For example, type "1,2,3" to include tracks 1 through 3."""
    tracks: NotRequired[
        "capo_mediaconvert.types.__list_of__integer_min1_max2147483647.__listOf__integerMin1Max2147483647"
    ]
    """Identify a track from the input audio to include in this selector by entering the track index number. These numberings include only tracks recognized as audio. If the service recognizes more types of audio tracks in the future, these numberings may shift. To include several tracks in a single audio selector, specify multiple tracks as follows. Using the console, enter a comma-separated list. For example, type "1,2,3" to include tracks 1 through 3."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSelector) -> dict:
    out: dict = {}
    if "audio_duration_correction" in value:
        import capo_mediaconvert.types.audio_duration_correction

        out["audioDurationCorrection"] = (
            capo_mediaconvert.types.audio_duration_correction.serialize_json(
                value["audio_duration_correction"]
            )
        )
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "default_selection" in value:
        import capo_mediaconvert.types.audio_default_selection

        out["defaultSelection"] = (
            capo_mediaconvert.types.audio_default_selection.serialize_json(
                value["default_selection"]
            )
        )
    if "external_audio_file_input" in value:
        out["externalAudioFileInput"] = value["external_audio_file_input"]
    if "hls_rendition_group_settings" in value:
        import capo_mediaconvert.types.hls_rendition_group_settings

        out["hlsRenditionGroupSettings"] = (
            capo_mediaconvert.types.hls_rendition_group_settings.serialize_json(
                value["hls_rendition_group_settings"]
            )
        )
    if "language_code" in value:
        import capo_mediaconvert.types.language_code

        out["languageCode"] = capo_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "offset" in value:
        out["offset"] = value["offset"]
    if "pids" in value:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["pids"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.serialize_json(
                value["pids"]
            )
        )
    if "program_selection" in value:
        out["programSelection"] = value["program_selection"]
    if "remix_settings" in value:
        import capo_mediaconvert.types.remix_settings

        out["remixSettings"] = capo_mediaconvert.types.remix_settings.serialize_json(
            value["remix_settings"]
        )
    if "selector_type" in value:
        import capo_mediaconvert.types.audio_selector_type

        out["selectorType"] = (
            capo_mediaconvert.types.audio_selector_type.serialize_json(
                value["selector_type"]
            )
        )
    if "smpte337_passthrough" in value:
        import capo_mediaconvert.types.audio_smpte337_passthrough

        out["smpte337Passthrough"] = (
            capo_mediaconvert.types.audio_smpte337_passthrough.serialize_json(
                value["smpte337_passthrough"]
            )
        )
    if "streams" in value:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["streams"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.serialize_json(
                value["streams"]
            )
        )
    if "tracks" in value:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["tracks"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.serialize_json(
                value["tracks"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSelector:
    out: AudioSelector = {}  # type: ignore[typeddict-item]
    if data.get("audioDurationCorrection") is not None:
        import capo_mediaconvert.types.audio_duration_correction

        out["audio_duration_correction"] = (
            capo_mediaconvert.types.audio_duration_correction.deserialize_json(
                data["audioDurationCorrection"]
            )
        )
    if data.get("customLanguageCode") is not None:
        out["custom_language_code"] = data["customLanguageCode"]
    if data.get("defaultSelection") is not None:
        import capo_mediaconvert.types.audio_default_selection

        out["default_selection"] = (
            capo_mediaconvert.types.audio_default_selection.deserialize_json(
                data["defaultSelection"]
            )
        )
    if data.get("externalAudioFileInput") is not None:
        out["external_audio_file_input"] = data["externalAudioFileInput"]
    if data.get("hlsRenditionGroupSettings") is not None:
        import capo_mediaconvert.types.hls_rendition_group_settings

        out["hls_rendition_group_settings"] = (
            capo_mediaconvert.types.hls_rendition_group_settings.deserialize_json(
                data["hlsRenditionGroupSettings"]
            )
        )
    if data.get("languageCode") is not None:
        import capo_mediaconvert.types.language_code

        out["language_code"] = capo_mediaconvert.types.language_code.deserialize_json(
            data["languageCode"]
        )
    if data.get("offset") is not None:
        out["offset"] = data["offset"]
    if data.get("pids") is not None:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["pids"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.deserialize_json(
                data["pids"]
            )
        )
    if data.get("programSelection") is not None:
        out["program_selection"] = data["programSelection"]
    if data.get("remixSettings") is not None:
        import capo_mediaconvert.types.remix_settings

        out["remix_settings"] = capo_mediaconvert.types.remix_settings.deserialize_json(
            data["remixSettings"]
        )
    if data.get("selectorType") is not None:
        import capo_mediaconvert.types.audio_selector_type

        out["selector_type"] = (
            capo_mediaconvert.types.audio_selector_type.deserialize_json(
                data["selectorType"]
            )
        )
    if data.get("smpte337Passthrough") is not None:
        import capo_mediaconvert.types.audio_smpte337_passthrough

        out["smpte337_passthrough"] = (
            capo_mediaconvert.types.audio_smpte337_passthrough.deserialize_json(
                data["smpte337Passthrough"]
            )
        )
    if data.get("streams") is not None:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["streams"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.deserialize_json(
                data["streams"]
            )
        )
    if data.get("tracks") is not None:
        import capo_mediaconvert.types.__list_of__integer_min1_max2147483647

        out["tracks"] = (
            capo_mediaconvert.types.__list_of__integer_min1_max2147483647.deserialize_json(
                data["tracks"]
            )
        )
    return out
