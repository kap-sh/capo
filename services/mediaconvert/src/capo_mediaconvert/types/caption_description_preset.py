"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionDescriptionPreset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__string_pattern_a_za_z23_a_za_z
    import capo_mediaconvert.types.caption_destination_settings
    import capo_mediaconvert.types.language_code


class CaptionDescriptionPreset(TypedDict, closed=True):
    custom_language_code: NotRequired[
        "capo_mediaconvert.types.__string_pattern_a_za_z23_a_za_z.__stringPatternAZaZ23AZaZ"
    ]
    """Specify the language for this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information when automatically selecting the font script for rendering the captions text. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming."""
    destination_settings: NotRequired[
        "capo_mediaconvert.types.caption_destination_settings.CaptionDestinationSettings"
    ]
    """Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html."""
    language_code: NotRequired["capo_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language of this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information to choose the font language for rendering the captions text."""
    language_description: NotRequired["capo_mediaconvert.types.__string.__string"]
    """Specify a label for this set of output captions. For example, "English", "Director commentary", or "track_2". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDescriptionPreset) -> dict:
    out: dict = {}
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "destination_settings" in value:
        import capo_mediaconvert.types.caption_destination_settings

        out["destinationSettings"] = (
            capo_mediaconvert.types.caption_destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "language_code" in value:
        import capo_mediaconvert.types.language_code

        out["languageCode"] = capo_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "language_description" in value:
        out["languageDescription"] = value["language_description"]
    return out


def deserialize_json(data: dict) -> CaptionDescriptionPreset:
    out: CaptionDescriptionPreset = {}  # type: ignore[typeddict-item]
    if data.get("customLanguageCode") is not None:
        out["custom_language_code"] = data["customLanguageCode"]
    if data.get("destinationSettings") is not None:
        import capo_mediaconvert.types.caption_destination_settings

        out["destination_settings"] = (
            capo_mediaconvert.types.caption_destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if data.get("languageCode") is not None:
        import capo_mediaconvert.types.language_code

        out["language_code"] = capo_mediaconvert.types.language_code.deserialize_json(
            data["languageCode"]
        )
    if data.get("languageDescription") is not None:
        out["language_description"] = data["languageDescription"]
    return out
