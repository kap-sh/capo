"""Generated from Smithy shape ``com.amazonaws.deadline#SearchTermFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.search_term
    import capo_deadline.types.search_term_matching_type


class SearchTermFilterExpression(TypedDict, closed=True):
    search_term: "capo_deadline.types.search_term.SearchTerm"
    """The term to search for."""
    match_type: "capo_deadline.types.search_term_matching_type.SearchTermMatchingType"
    """<p>Specifies how Deadline Cloud matches your search term in the results. If you don't specify a <code>matchType</code> the default is <code>FUZZY_MATCH</code>.</p> <ul> <li> <p> <code>FUZZY_MATCH</code> - Matches if a portion of the search term is found in the result.</p> </li> <li> <p> <code>CONTAINS</code> - Matches if the exact search term is contained in the result.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTermFilterExpression) -> dict:
    out: dict = {}
    out["searchTerm"] = value["search_term"]
    import capo_deadline.types.search_term_matching_type

    out["matchType"] = capo_deadline.types.search_term_matching_type.serialize_json(
        value.get("match_type", "FUZZY_MATCH")
    )
    return out


def deserialize_json(data: dict) -> SearchTermFilterExpression:
    out: SearchTermFilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("searchTerm") is not None:
        out["search_term"] = data["searchTerm"]
    else:
        out["search_term"] = ""
    if data.get("matchType") is not None:
        import capo_deadline.types.search_term_matching_type

        out["match_type"] = (
            capo_deadline.types.search_term_matching_type.deserialize_json(
                data["matchType"]
            )
        )
    else:
        out["match_type"] = "FUZZY_MATCH"
    return out
