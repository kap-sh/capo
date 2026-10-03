"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_video_overlay_input_clipping
    import capo_mediaconvert.types.__map_of_audio_selector
    import capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d
    import capo_mediaconvert.types.__string_pattern_s3_https
    import capo_mediaconvert.types.input_timecode_source


class VideoOverlayInput(TypedDict, closed=True):
    audio_selectors: NotRequired[
        "capo_mediaconvert.types.__map_of_audio_selector.__mapOfAudioSelector"
    ]
    r"""Use Audio selectors to specify audio to use during your Video overlay. You can use multiple Audio selectors per Video overlay. When you include an Audio selector within a Video overlay, MediaConvert mutes any Audio selectors with the same name from the underlying input. For example, if your underlying input has Audio selector 1 and Audio selector 2, and your Video overlay only has Audio selector 1, then MediaConvert replaces all audio for Audio selector 1 during the Video overlay. To replace all audio for all Audio selectors from the underlying input by using a single Audio selector in your overlay, set DefaultSelection to DEFAULT (Check \"Use as default\" in the MediaConvert console)."""
    file_input: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_https.__stringPatternS3Https"
    ]
    """Specify the input file S3, HTTP, or HTTPS URL for your video overlay. To specify one or more Transitions for your base input video instead: Leave blank."""
    input_clippings: NotRequired[
        "capo_mediaconvert.types.__list_of_video_overlay_input_clipping.__listOfVideoOverlayInputClipping"
    ]
    """Specify one or more clips to use from your video overlay. When you include an input clip, you must also specify its start timecode, end timecode, or both start and end timecode."""
    timecode_source: NotRequired[
        "capo_mediaconvert.types.input_timecode_source.InputTimecodeSource"
    ]
    """Specify the timecode source for your video overlay input clips. To use the timecode present in your video overlay: Choose Embedded. To use a zerobased timecode: Choose Start at 0. To choose a timecode: Choose Specified start. When you do, enter the starting timecode in Start timecode. If you don't specify a value for Timecode source, MediaConvert uses Embedded by default."""
    timecode_start: NotRequired[
        "capo_mediaconvert.types.__string_min11_max11_pattern01_d20305_d205_d.__stringMin11Max11Pattern01D20305D205D"
    ]
    """Specify the starting timecode for this video overlay. To use this setting, you must set Timecode source to Specified start."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayInput) -> dict:
    out: dict = {}
    if "audio_selectors" in value:
        import capo_mediaconvert.types.__map_of_audio_selector

        out["audioSelectors"] = (
            capo_mediaconvert.types.__map_of_audio_selector.serialize_json(
                value["audio_selectors"]
            )
        )
    if "file_input" in value:
        out["fileInput"] = value["file_input"]
    if "input_clippings" in value:
        import capo_mediaconvert.types.__list_of_video_overlay_input_clipping

        out["inputClippings"] = (
            capo_mediaconvert.types.__list_of_video_overlay_input_clipping.serialize_json(
                value["input_clippings"]
            )
        )
    if "timecode_source" in value:
        import capo_mediaconvert.types.input_timecode_source

        out["timecodeSource"] = (
            capo_mediaconvert.types.input_timecode_source.serialize_json(
                value["timecode_source"]
            )
        )
    if "timecode_start" in value:
        out["timecodeStart"] = value["timecode_start"]
    return out


def deserialize_json(data: dict) -> VideoOverlayInput:
    out: VideoOverlayInput = {}  # type: ignore[typeddict-item]
    if data.get("audioSelectors") is not None:
        import capo_mediaconvert.types.__map_of_audio_selector

        out["audio_selectors"] = (
            capo_mediaconvert.types.__map_of_audio_selector.deserialize_json(
                data["audioSelectors"]
            )
        )
    if data.get("fileInput") is not None:
        out["file_input"] = data["fileInput"]
    if data.get("inputClippings") is not None:
        import capo_mediaconvert.types.__list_of_video_overlay_input_clipping

        out["input_clippings"] = (
            capo_mediaconvert.types.__list_of_video_overlay_input_clipping.deserialize_json(
                data["inputClippings"]
            )
        )
    if data.get("timecodeSource") is not None:
        import capo_mediaconvert.types.input_timecode_source

        out["timecode_source"] = (
            capo_mediaconvert.types.input_timecode_source.deserialize_json(
                data["timecodeSource"]
            )
        )
    if data.get("timecodeStart") is not None:
        out["timecode_start"] = data["timecodeStart"]
    return out
