"""Generated from Smithy shape ``com.amazonaws.deadline#SearchWorkersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_item_offset
    import capo_deadline.types.total_results
    import capo_deadline.types.worker_search_summaries


class SearchWorkersResponse(TypedDict, closed=True):
    workers: "capo_deadline.types.worker_search_summaries.WorkerSearchSummaries"
    """The workers for the search."""
    next_item_offset: NotRequired["capo_deadline.types.next_item_offset.NextItemOffset"]
    """The next item offset for the search results."""
    total_results: "capo_deadline.types.total_results.TotalResults"
    """The total number of results in the search."""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkersResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.worker_search_summaries

    out["workers"] = capo_deadline.types.worker_search_summaries.serialize_json(
        value["workers"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchWorkersResponse:
    out: SearchWorkersResponse = {}  # type: ignore[typeddict-item]
    if data.get("workers") is not None:
        import capo_deadline.types.worker_search_summaries

        out["workers"] = capo_deadline.types.worker_search_summaries.deserialize_json(
            data["workers"]
        )
    else:
        out["workers"] = []
    if data.get("nextItemOffset") is not None:
        out["next_item_offset"] = data["nextItemOffset"]
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    else:
        out["total_results"] = 0
    return out
