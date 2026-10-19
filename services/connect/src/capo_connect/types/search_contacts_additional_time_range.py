"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsAdditionalTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_additional_time_range_criteria_list
    import capo_connect.types.search_contacts_match_type


class SearchContactsAdditionalTimeRange(TypedDict, closed=True):
    criteria: "capo_connect.types.search_contacts_additional_time_range_criteria_list.SearchContactsAdditionalTimeRangeCriteriaList"
    """<p>List of criteria of the time range to additionally filter on.</p>"""
    match_type: "capo_connect.types.search_contacts_match_type.SearchContactsMatchType"
    """<p>The match type combining multiple time range filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsAdditionalTimeRange) -> dict:
    out: dict = {}
    import capo_connect.types.search_contacts_additional_time_range_criteria_list

    out["Criteria"] = (
        capo_connect.types.search_contacts_additional_time_range_criteria_list.serialize_json(
            value["criteria"]
        )
    )
    import capo_connect.types.search_contacts_match_type

    out["MatchType"] = capo_connect.types.search_contacts_match_type.serialize_json(
        value["match_type"]
    )
    return out


def deserialize_json(data: dict) -> SearchContactsAdditionalTimeRange:
    out: SearchContactsAdditionalTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("Criteria") is not None:
        import capo_connect.types.search_contacts_additional_time_range_criteria_list

        out["criteria"] = (
            capo_connect.types.search_contacts_additional_time_range_criteria_list.deserialize_json(
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
    else:
        import typing

        out["match_type"] = typing.cast(
            "capo_connect.types.search_contacts_match_type.SearchContactsMatchType", ""
        )
    return out
