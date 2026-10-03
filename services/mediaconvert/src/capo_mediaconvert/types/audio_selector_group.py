"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioSelectorGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of__string_min1


class AudioSelectorGroup(TypedDict, closed=True):
    audio_selector_names: NotRequired[
        "capo_mediaconvert.types.__list_of__string_min1.__listOf__stringMin1"
    ]
    """Name of an Audio Selector within the same input to include in the group. Audio selector names are standardized, based on their order within the input (e.g., "Audio Selector 1"). The audio selector name parameter can be repeated to add any number of audio selectors to the group."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSelectorGroup) -> dict:
    out: dict = {}
    if "audio_selector_names" in value:
        import capo_mediaconvert.types.__list_of__string_min1

        out["audioSelectorNames"] = (
            capo_mediaconvert.types.__list_of__string_min1.serialize_json(
                value["audio_selector_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioSelectorGroup:
    out: AudioSelectorGroup = {}  # type: ignore[typeddict-item]
    if data.get("audioSelectorNames") is not None:
        import capo_mediaconvert.types.__list_of__string_min1

        out["audio_selector_names"] = (
            capo_mediaconvert.types.__list_of__string_min1.deserialize_json(
                data["audioSelectorNames"]
            )
        )
    return out
