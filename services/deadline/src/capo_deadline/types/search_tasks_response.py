"""Generated from Smithy shape ``com.amazonaws.deadline#SearchTasksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_item_offset
    import capo_deadline.types.task_search_summaries
    import capo_deadline.types.total_results


class SearchTasksResponse(TypedDict, closed=True):
    tasks: "capo_deadline.types.task_search_summaries.TaskSearchSummaries"
    """<p>Tasks in the search.</p>"""
    next_item_offset: NotRequired["capo_deadline.types.next_item_offset.NextItemOffset"]
    """<p>The next item offset for the search results.</p>"""
    total_results: "capo_deadline.types.total_results.TotalResults"
    """<p>The total number of results in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTasksResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.task_search_summaries

    out["tasks"] = capo_deadline.types.task_search_summaries.serialize_json(
        value["tasks"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchTasksResponse:
    out: SearchTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_deadline.types.task_search_summaries

        out["tasks"] = capo_deadline.types.task_search_summaries.deserialize_json(
            data["tasks"]
        )
    else:
        out["tasks"] = []
    if data.get("nextItemOffset") is not None:
        out["next_item_offset"] = data["nextItemOffset"]
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    else:
        out["total_results"] = 0
    return out


def redact_sensitive(value: SearchTasksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tasks" in value:
        import capo_deadline.types.task_search_summaries

        out["tasks"] = capo_deadline.types.task_search_summaries.redact_sensitive(
            value["tasks"]
        )
    return out
