"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionarySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_arn
    import capo_elementalinference.types.dictionary_id
    import capo_elementalinference.types.dictionary_language
    import capo_elementalinference.types.dictionary_status
    import capo_elementalinference.types.resource_name


class DictionarySummary(TypedDict, closed=True):
    arn: "capo_elementalinference.types.dictionary_arn.DictionaryArn"
    """<p>The ARN of the dictionary.</p>"""
    id: "capo_elementalinference.types.dictionary_id.DictionaryId"
    """<p>The ID of the dictionary.</p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the dictionary.</p>"""
    language: "capo_elementalinference.types.dictionary_language.DictionaryLanguage"
    """<p>The language of the dictionary.</p>"""
    status: "capo_elementalinference.types.dictionary_status.DictionaryStatus"
    """<p>The status of the dictionary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DictionarySummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_elementalinference.types.dictionary_language

    out["language"] = capo_elementalinference.types.dictionary_language.serialize_json(
        value["language"]
    )
    import capo_elementalinference.types.dictionary_status

    out["status"] = capo_elementalinference.types.dictionary_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DictionarySummary:
    out: DictionarySummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
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
    if data.get("status") is not None:
        import capo_elementalinference.types.dictionary_status

        out["status"] = (
            capo_elementalinference.types.dictionary_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.dictionary_status.DictionaryStatus", ""
        )
    return out
