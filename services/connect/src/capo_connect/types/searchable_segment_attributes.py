"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_match_type
    import capo_connect.types.searchable_segment_attributes_criteria_list


class SearchableSegmentAttributes(TypedDict, closed=True):
    criteria: "capo_connect.types.searchable_segment_attributes_criteria_list.SearchableSegmentAttributesCriteriaList"
    """<p>The list of criteria based on searchable segment attributes.</p>"""
    match_type: NotRequired[
        "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining search criteria using multiple searchable segment attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributes) -> dict:
    out: dict = {}
    import capo_connect.types.searchable_segment_attributes_criteria_list

    out["Criteria"] = (
        capo_connect.types.searchable_segment_attributes_criteria_list.serialize_json(
            value["criteria"]
        )
    )
    if "match_type" in value:
        import capo_connect.types.search_contacts_match_type

        out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
            value["match_type"]
        )
    return out


def deserialize_json(data: dict) -> SearchableSegmentAttributes:
    out: SearchableSegmentAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Criteria") is not None:
        import capo_connect.types.searchable_segment_attributes_criteria_list

        out["criteria"] = (
            capo_connect.types.searchable_segment_attributes_criteria_list.deserialize_json(
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


def redact_sensitive(value: SearchableSegmentAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "criteria" in value:
        import capo_connect.types.searchable_segment_attributes_criteria_list

        out["criteria"] = (
            capo_connect.types.searchable_segment_attributes_criteria_list.redact_sensitive(
                value["criteria"]
            )
        )
    return out
