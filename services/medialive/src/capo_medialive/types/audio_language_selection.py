"""Generated from Smithy shape ``com.amazonaws.medialive#AudioLanguageSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.audio_language_selection_policy


class AudioLanguageSelection(TypedDict, closed=True):
    language_code: NotRequired["capo_medialive.types.__string.__string"]
    """Selects a specific three-letter language code from within an audio source."""
    language_selection_policy: NotRequired[
        "capo_medialive.types.audio_language_selection_policy.AudioLanguageSelectionPolicy"
    ]
    """When set to "strict", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If "loose", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioLanguageSelection) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "language_selection_policy" in value:
        import capo_medialive.types.audio_language_selection_policy

        out["languageSelectionPolicy"] = (
            capo_medialive.types.audio_language_selection_policy.serialize_json(
                value["language_selection_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioLanguageSelection:
    out: AudioLanguageSelection = {}  # type: ignore[typeddict-item]
    if data.get("languageCode") is not None:
        out["language_code"] = data["languageCode"]
    if data.get("languageSelectionPolicy") is not None:
        import capo_medialive.types.audio_language_selection_policy

        out["language_selection_policy"] = (
            capo_medialive.types.audio_language_selection_policy.deserialize_json(
                data["languageSelectionPolicy"]
            )
        )
    return out
