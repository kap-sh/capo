"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimecodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern010920405090509092
    import capo_mediaconvert.types.__string_pattern0940191020191209301
    import capo_mediaconvert.types.timecode_source


class TimecodeConfig(TypedDict, closed=True):
    anchor: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """If you use an editing platform that relies on an anchor timecode, use Anchor Timecode to specify a timecode that will match the input video frame to the output video frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF). This setting ignores frame rate conversion. System behavior for Anchor Timecode varies depending on your setting for Source. * If Source is set to Specified Start, the first input frame is the specified value in Start Timecode. Anchor Timecode and Start Timecode are used calculate output timecode. * If Source is set to Start at 0 the first frame is 00:00:00:00. * If Source is set to Embedded, the first frame is the timecode value on the first input frame of the input."""
    source: NotRequired["capo_mediaconvert.types.timecode_source.TimecodeSource"]
    """Use Source to set how timecodes are handled within this job. To make sure that your video, audio, captions, and markers are synchronized and that time-based features, such as image inserter, work correctly, choose the Timecode source option that matches your assets. All timecodes are in a 24-hour format with frame number (HH:MM:SS:FF). * Embedded - Use the timecode that is in the input video. If no embedded timecode is in the source, the service will use Start at 0 instead. * Start at 0 - Set the timecode of the initial frame to 00:00:00:00. * Specified Start - Set the timecode of the initial frame to a value other than zero. You use Start timecode to provide this value."""
    start: NotRequired[
        "capo_mediaconvert.types.__string_pattern010920405090509092.__stringPattern010920405090509092"
    ]
    """Only use when you set Source to Specified start. Use Start timecode to specify the timecode for the initial frame. Use 24-hour format with frame number, (HH:MM:SS:FF) or (HH:MM:SS;FF)."""
    timestamp_offset: NotRequired[
        "capo_mediaconvert.types.__string_pattern0940191020191209301.__stringPattern0940191020191209301"
    ]
    """Only applies to outputs that support program-date-time stamp. Use Timestamp offset to overwrite the timecode date without affecting the time and frame number. Provide the new date as a string in the format "yyyy-mm-dd". To use Timestamp offset, you must also enable Insert program-date-time in the output settings. For example, if the date part of your timecodes is 2002-1-25 and you want to change it to one year later, set Timestamp offset to 2003-1-25."""


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeConfig) -> dict:
    out: dict = {}
    if "anchor" in value:
        out["anchor"] = value["anchor"]
    if "source" in value:
        import capo_mediaconvert.types.timecode_source

        out["source"] = capo_mediaconvert.types.timecode_source.serialize_json(
            value["source"]
        )
    if "start" in value:
        out["start"] = value["start"]
    if "timestamp_offset" in value:
        out["timestampOffset"] = value["timestamp_offset"]
    return out


def deserialize_json(data: dict) -> TimecodeConfig:
    out: TimecodeConfig = {}  # type: ignore[typeddict-item]
    if data.get("anchor") is not None:
        out["anchor"] = data["anchor"]
    if data.get("source") is not None:
        import capo_mediaconvert.types.timecode_source

        out["source"] = capo_mediaconvert.types.timecode_source.deserialize_json(
            data["source"]
        )
    if data.get("start") is not None:
        out["start"] = data["start"]
    if data.get("timestampOffset") is not None:
        out["timestamp_offset"] = data["timestampOffset"]
    return out
