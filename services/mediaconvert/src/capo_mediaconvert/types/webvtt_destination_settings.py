"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WebvttDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.webvtt_accessibility_subs
    import capo_mediaconvert.types.webvtt_style_passthrough


class WebvttDestinationSettings(TypedDict, closed=True):
    accessibility: NotRequired[
        "capo_mediaconvert.types.webvtt_accessibility_subs.WebvttAccessibilitySubs"
    ]
    """If the WebVTT captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>."""
    style_passthrough: NotRequired[
        "capo_mediaconvert.types.webvtt_style_passthrough.WebvttStylePassthrough"
    ]
    """Specify how MediaConvert writes style information in your output WebVTT captions. To use the available style, color, and position information from your input captions: Choose Enabled. MediaConvert uses default settings when style and position information is missing from your input captions. To recreate the input captions exactly: Choose Strict. MediaConvert automatically applies timing adjustments, including adjustments for frame rate conversion, ad avails, and input clipping. Your input captions format must be WebVTT. To ignore the style and position information from your input captions and use simplified output captions: Keep the default value, Disabled. Or leave blank. To use the available style, color, and position information from your input captions, while merging cues with identical time ranges: Choose merge. This setting can help prevent positioning overlaps for certain players that expect a single single cue for any given time range."""


# --- restJson1 ser/de ---
def serialize_json(value: WebvttDestinationSettings) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import capo_mediaconvert.types.webvtt_accessibility_subs

        out["accessibility"] = (
            capo_mediaconvert.types.webvtt_accessibility_subs.serialize_json(
                value["accessibility"]
            )
        )
    if "style_passthrough" in value:
        import capo_mediaconvert.types.webvtt_style_passthrough

        out["stylePassthrough"] = (
            capo_mediaconvert.types.webvtt_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebvttDestinationSettings:
    out: WebvttDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("accessibility") is not None:
        import capo_mediaconvert.types.webvtt_accessibility_subs

        out["accessibility"] = (
            capo_mediaconvert.types.webvtt_accessibility_subs.deserialize_json(
                data["accessibility"]
            )
        )
    if data.get("stylePassthrough") is not None:
        import capo_mediaconvert.types.webvtt_style_passthrough

        out["style_passthrough"] = (
            capo_mediaconvert.types.webvtt_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    return out
