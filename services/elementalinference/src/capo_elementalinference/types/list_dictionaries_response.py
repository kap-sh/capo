"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListDictionariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.dictionary_summary_list


class ListDictionariesResponse(TypedDict, closed=True):
    dictionaries: (
        "capo_elementalinference.types.dictionary_summary_list.DictionarySummaryList"
    )
    """<p>A list of DictionarySummary objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use to retrieve the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDictionariesResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.dictionary_summary_list

    out["dictionaries"] = (
        capo_elementalinference.types.dictionary_summary_list.serialize_json(
            value["dictionaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDictionariesResponse:
    out: ListDictionariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("dictionaries") is not None:
        import capo_elementalinference.types.dictionary_summary_list

        out["dictionaries"] = (
            capo_elementalinference.types.dictionary_summary_list.deserialize_json(
                data["dictionaries"]
            )
        )
    else:
        out["dictionaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
