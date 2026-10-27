"""Generated from Smithy shape ``com.amazonaws.deadline#SearchStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_item_offset
    import capo_deadline.types.step_search_summaries
    import capo_deadline.types.total_results


class SearchStepsResponse(TypedDict, closed=True):
    steps: "capo_deadline.types.step_search_summaries.StepSearchSummaries"
    """The steps in the search."""
    next_item_offset: NotRequired["capo_deadline.types.next_item_offset.NextItemOffset"]
    """The next item offset for the search results."""
    total_results: "capo_deadline.types.total_results.TotalResults"
    """The total number of results in the search."""


# --- restJson1 ser/de ---
def serialize_json(value: SearchStepsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.step_search_summaries

    out["steps"] = capo_deadline.types.step_search_summaries.serialize_json(
        value["steps"]
    )
    if "next_item_offset" in value:
        out["nextItemOffset"] = value["next_item_offset"]
    out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchStepsResponse:
    out: SearchStepsResponse = {}  # type: ignore[typeddict-item]
    if data.get("steps") is not None:
        import capo_deadline.types.step_search_summaries

        out["steps"] = capo_deadline.types.step_search_summaries.deserialize_json(
            data["steps"]
        )
    else:
        out["steps"] = []
    if data.get("nextItemOffset") is not None:
        out["next_item_offset"] = data["nextItemOffset"]
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    else:
        out["total_results"] = 0
    return out
