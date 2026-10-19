"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListSearchesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.search_summaries


class ListSearchesResponse(TypedDict, closed=True):
    search_summaries: "capo_iotsitewise.types.search_summaries.SearchSummaries"
    """<p>A page of search summaries, most recently started first.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The pagination token to use in a subsequent ListSearches call to retrieve the next page. Absent when there are no more searches.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSearchesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.search_summaries

    out["searchSummaries"] = capo_iotsitewise.types.search_summaries.serialize_json(
        value["search_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSearchesResponse:
    out: ListSearchesResponse = {}  # type: ignore[typeddict-item]
    if data.get("searchSummaries") is not None:
        import capo_iotsitewise.types.search_summaries

        out["search_summaries"] = (
            capo_iotsitewise.types.search_summaries.deserialize_json(
                data["searchSummaries"]
            )
        )
    else:
        out["search_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSearchesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "search_summaries" in value:
        import capo_iotsitewise.types.search_summaries

        out["search_summaries"] = (
            capo_iotsitewise.types.search_summaries.redact_sensitive(
                value["search_summaries"]
            )
        )
    return out
