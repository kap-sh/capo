"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetSearchResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.search_result_list


class GetSearchResultsResponse(TypedDict, closed=True):
    search_results: "capo_iotsitewise.types.search_result_list.SearchResultList"
    """<p>A page of search results, ordered by descending relevance score.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The pagination token to use in a subsequent GetSearchResults call to retrieve the next page. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchResultsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.search_result_list

    out["searchResults"] = capo_iotsitewise.types.search_result_list.serialize_json(
        value["search_results"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSearchResultsResponse:
    out: GetSearchResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("searchResults") is not None:
        import capo_iotsitewise.types.search_result_list

        out["search_results"] = (
            capo_iotsitewise.types.search_result_list.deserialize_json(
                data["searchResults"]
            )
        )
    else:
        out["search_results"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
