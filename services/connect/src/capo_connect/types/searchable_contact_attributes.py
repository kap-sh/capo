"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.searchable_contact_attributes_criteria_list


class SearchableContactAttributes(TypedDict, closed=True):
    criteria: "capo_connect.types.searchable_contact_attributes_criteria_list.SearchableContactAttributesCriteriaList"
    """<p>The list of criteria based on user-defined contact attributes that are configured for contact search.</p>"""
    match_type: NotRequired[
        "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple searchable contact attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributes) -> dict:
    out: dict = {}
    import capo_connect.types.searchable_contact_attributes_criteria_list

    out["Criteria"] = (
        capo_connect.types.searchable_contact_attributes_criteria_list.serialize_json(
            value["criteria"]
        )
    )
    if "match_type" in value:
        import capo_connect.types.search_contacts_match_type

        out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
            value["match_type"]
        )
    return out


def deserialize_json(data: dict) -> SearchableContactAttributes:
    out: SearchableContactAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Criteria") is not None:
        import capo_connect.types.searchable_contact_attributes_criteria_list

        out["criteria"] = (
            capo_connect.types.searchable_contact_attributes_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    else:
        out["criteria"] = []
    if data.get("MatchType") is not None:
        import capo_connect.types.search_contacts_match_type

        out["match_type"] = (
            capo_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out


def redact_sensitive(value: SearchableContactAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "criteria" in value:
        import capo_connect.types.searchable_contact_attributes_criteria_list

        out["criteria"] = (
            capo_connect.types.searchable_contact_attributes_criteria_list.redact_sensitive(
                value["criteria"]
            )
        )
    return out
