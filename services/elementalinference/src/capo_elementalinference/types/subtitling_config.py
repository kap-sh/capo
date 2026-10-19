"""Generated from Smithy shape ``com.amazonaws.elementalinference#SubtitlingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.aspect_ratio
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.profanity_filter_mode
    import capo_elementalinference.types.transcription_language


class SubtitlingConfig(TypedDict, closed=True):
    language: (
        "capo_elementalinference.types.transcription_language.TranscriptionLanguage"
    )
    """<p>The language of the audio in the source media. Elemental Inference uses this setting to optimize transcription accuracy. Specify the language using an ISO 639-2/T three-letter code, optionally with a region subtag. Supported values: eng, eng-au, eng-gb, eng-us, fra, ita, deu, spa, por. </p>"""
    aspect_ratio: NotRequired["capo_elementalinference.types.aspect_ratio.AspectRatio"]
    """<p>The aspect ratio of the output video, specified as width and height integer values. Elemental Inference uses the aspect ratio to determine subtitle layout and line lengths. </p>"""
    dictionary: NotRequired["capo_elementalinference.types.dictionary_id.DictionaryId"]
    """<p>The ID of a custom dictionary to improve transcription accuracy for domain-specific terminology. Use the CreateDictionary operation to create a dictionary. </p>"""
    profanity_filter: NotRequired[
        "capo_elementalinference.types.profanity_filter_mode.ProfanityFilterMode"
    ]
    """<p>Controls how profanity is handled in the generated subtitles. Valid values: DISABLED (no filtering, default), CENSOR (replace profanity with asterisks), DROP (remove profanity from the transcript). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubtitlingConfig) -> dict:
    out: dict = {}
    import capo_elementalinference.types.transcription_language

    out["language"] = (
        capo_elementalinference.types.transcription_language.serialize_json(
            value["language"]
        )
    )
    if "aspect_ratio" in value:
        import capo_elementalinference.types.aspect_ratio

        out["aspectRatio"] = capo_elementalinference.types.aspect_ratio.serialize_json(
            value["aspect_ratio"]
        )
    if "dictionary" in value:
        out["dictionary"] = value["dictionary"]
    if "profanity_filter" in value:
        import capo_elementalinference.types.profanity_filter_mode

        out["profanityFilter"] = (
            capo_elementalinference.types.profanity_filter_mode.serialize_json(
                value["profanity_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubtitlingConfig:
    out: SubtitlingConfig = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        import capo_elementalinference.types.transcription_language

        out["language"] = (
            capo_elementalinference.types.transcription_language.deserialize_json(
                data["language"]
            )
        )
    else:
        import typing

        out["language"] = typing.cast(
            "capo_elementalinference.types.transcription_language.TranscriptionLanguage",
            "",
        )
    if data.get("aspectRatio") is not None:
        import capo_elementalinference.types.aspect_ratio

        out["aspect_ratio"] = (
            capo_elementalinference.types.aspect_ratio.deserialize_json(
                data["aspectRatio"]
            )
        )
    if data.get("dictionary") is not None:
        out["dictionary"] = data["dictionary"]
    if data.get("profanityFilter") is not None:
        import capo_elementalinference.types.profanity_filter_mode

        out["profanity_filter"] = (
            capo_elementalinference.types.profanity_filter_mode.deserialize_json(
                data["profanityFilter"]
            )
        )
    return out
