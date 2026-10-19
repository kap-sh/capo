"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateDictionaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_entries_payload
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class CreateDictionaryRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this dictionary.</p>"""
    language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
    """<p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>"""
    entries: NotRequired[
        "capo_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
    ]
    """<p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the dictionary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDictionaryRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_elementalinference.types.dictionary_language

    out["language"] = capo_elementalinference.types.dictionary_language.serialize_json(
        value["language"]
    )
    if "entries" in value:
        out["entries"] = value["entries"]
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDictionaryRequest:
    out: CreateDictionaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("language") is not None:
        import capo_elementalinference.types.dictionary_language

        out["language"] = (
            capo_elementalinference.types.dictionary_language.deserialize_json(
                data["language"]
            )
        )
    else:
        import typing

        out["language"] = typing.cast(
            "capo_elementalinference.types.dictionary_language.DictionaryLanguage", ""
        )
    if data.get("entries") is not None:
        out["entries"] = data["entries"]
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
