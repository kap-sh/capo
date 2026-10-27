"""Generated from Smithy shape ``com.amazonaws.deadline#SearchJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_search_summaries
    import capo_deadline.types.next_item_offset
    import capo_deadline.types.total_results


class SearchJobsResponse(TypedDict, closed=True):
    jobs: "capo_deadline.types.job_search_summaries.JobSearchSummaries"
    """The jobs in the search."""
    next_item_offset: NotRequired["capo_deadline.types.next_item_offset.NextItemOffset"]
    """The next item offset for the search results."""
    total_results: "capo_deadline.types.total_results.TotalResults"
    """The total number of results in the search."""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.job_search_summaries

    out["jobs"] = capo_deadline.types.job_search_summaries.serialize_json(value["jobs"])
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchJobsResponse:
    out: SearchJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_deadline.types.job_search_summaries

        out["jobs"] = capo_deadline.types.job_search_summaries.deserialize_json(
            data["jobs"]
        )
    else:
        out["jobs"] = []
    if data.get("nextItemOffset") is not None:
        out["next_item_offset"] = data["nextItemOffset"]
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    else:
        out["total_results"] = 0
    return out


def redact_sensitive(value: SearchJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_deadline.types.job_search_summaries

        out["jobs"] = capo_deadline.types.job_search_summaries.redact_sensitive(
            value["jobs"]
        )
    return out
