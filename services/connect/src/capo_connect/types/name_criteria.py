"""Generated from Smithy shape ``com.amazonaws.connect#NameCriteria``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.search_text_list


class NameCriteria(TypedDict, closed=True):
    search_text: "capo_connect.types.search_text_list.SearchTextList"
    """<p>The words or phrases used to match the contact name.</p>"""
    match_type: "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    """<p>The match type combining name search criteria using multiple search texts in a name criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NameCriteria) -> dict:
    out: dict = {}
    import capo_connect.types.search_text_list

    out["SearchText"] = capo_connect.types.search_text_list.serialize_json(
        value["search_text"]
    )
    import capo_connect.types.search_contacts_match_type

    out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
        value["match_type"]
    )
    return out


def deserialize_json(data: dict) -> NameCriteria:
    out: NameCriteria = {}  # type: ignore[typeddict-item]
    if data.get("SearchText") is not None:
        import capo_connect.types.search_text_list

        out["search_text"] = capo_connect.types.search_text_list.deserialize_json(
            data["SearchText"]
        )
    else:
        raise DeserializationError("NameCriteria.search_text required")
    if data.get("MatchType") is not None:
        import capo_connect.types.search_contacts_match_type

        out["match_type"] = (
            capo_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    else:
        raise DeserializationError("NameCriteria.match_type required")
    return out


def redact_sensitive(value: NameCriteria) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_text" in value:
        import capo_connect.types.search_text_list

        out["search_text"] = capo_connect.types.search_text_list.redact_sensitive(
            value["search_text"]
        )
    return out
