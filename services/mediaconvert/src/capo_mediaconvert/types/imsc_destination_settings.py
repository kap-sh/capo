"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ImscDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.imsc_accessibility_subs
    import capo_mediaconvert.types.imsc_style_passthrough


class ImscDestinationSettings(TypedDict, closed=True):
    accessibility: NotRequired[
        "capo_mediaconvert.types.imsc_accessibility_subs.ImscAccessibilitySubs"
    ]
    """If the IMSC captions track is intended to provide accessibility for people who are deaf or hard of hearing: Set Accessibility subtitles to Enabled. When you do, MediaConvert adds accessibility attributes to your output HLS or DASH manifest. For HLS manifests, MediaConvert adds the following accessibility attributes under EXT-X-MEDIA for this track: CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound" and AUTOSELECT="YES". For DASH manifests, MediaConvert adds the following in the adaptation set for this track: <Accessibility schemeIdUri="urn:mpeg:dash:role:2011" value="caption"/>. If the captions track is not intended to provide such accessibility: Keep the default value, Disabled. When you do, for DASH manifests, MediaConvert instead adds the following in the adaptation set for this track: <Role schemeIDUri="urn:mpeg:dash:role:2011" value="subtitle"/>."""
    style_passthrough: NotRequired[
        "capo_mediaconvert.types.imsc_style_passthrough.ImscStylePassthrough"
    ]
    """Keep this setting enabled to have MediaConvert use the font style and position information from the captions source in the output. This option is available only when your input captions are IMSC, SMPTE-TT, or TTML. Disable this setting for simplified output captions."""


# --- restJson1 ser/de ---
def serialize_json(value: ImscDestinationSettings) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import capo_mediaconvert.types.imsc_accessibility_subs

        out["accessibility"] = (
            capo_mediaconvert.types.imsc_accessibility_subs.serialize_json(
                value["accessibility"]
            )
        )
    if "style_passthrough" in value:
        import capo_mediaconvert.types.imsc_style_passthrough

        out["stylePassthrough"] = (
            capo_mediaconvert.types.imsc_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImscDestinationSettings:
    out: ImscDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("accessibility") is not None:
        import capo_mediaconvert.types.imsc_accessibility_subs

        out["accessibility"] = (
            capo_mediaconvert.types.imsc_accessibility_subs.deserialize_json(
                data["accessibility"]
            )
        )
    if data.get("stylePassthrough") is not None:
        import capo_mediaconvert.types.imsc_style_passthrough

        out["style_passthrough"] = (
            capo_mediaconvert.types.imsc_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    return out
