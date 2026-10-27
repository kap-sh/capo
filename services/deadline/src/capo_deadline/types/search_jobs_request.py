"""Generated from Smithy shape ``com.amazonaws.deadline#SearchJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.integer
    import capo_deadline.types.queue_ids
    import capo_deadline.types.search_grouped_filter_expressions
    import capo_deadline.types.search_sort_expressions


class SearchJobsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the job."""
    filter_expressions: NotRequired[
        "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
    ]
    """The search terms for a resource."""
    sort_expressions: NotRequired[
        "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
    ]
    """The search terms for a resource."""
    item_offset: "capo_deadline.types.integer.Integer"
    """The offset for the search results."""
    page_size: NotRequired["capo_deadline.types.integer.Integer"]
    """Specifies the number of results to return."""
    queue_ids: "capo_deadline.types.queue_ids.QueueIds"
    """The queue ID to use in the job search."""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsRequest) -> dict:
    out: dict = {}
    if "filter_expressions" in value:
        import capo_deadline.types.search_grouped_filter_expressions

        out["filterExpressions"] = (
            capo_deadline.types.search_grouped_filter_expressions.serialize_json(
                value["filter_expressions"]
            )
        )
    if "sort_expressions" in value:
        import capo_deadline.types.search_sort_expressions

        out["sortExpressions"] = (
            capo_deadline.types.search_sort_expressions.serialize_json(
                value["sort_expressions"]
            )
        )
    out["itemOffset"] = value["item_offset"]
    if "page_size" in value:
        out["pageSize"] = value["page_size"]
    import capo_deadline.types.queue_ids

    out["queueIds"] = capo_deadline.types.queue_ids.serialize_json(value["queue_ids"])
    return out


def deserialize_json(data: dict) -> SearchJobsRequest:
    out: SearchJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterExpressions") is not None:
        import capo_deadline.types.search_grouped_filter_expressions

        out["filter_expressions"] = (
            capo_deadline.types.search_grouped_filter_expressions.deserialize_json(
                data["filterExpressions"]
            )
        )
    if data.get("sortExpressions") is not None:
        import capo_deadline.types.search_sort_expressions

        out["sort_expressions"] = (
            capo_deadline.types.search_sort_expressions.deserialize_json(
                data["sortExpressions"]
            )
        )
    if data.get("itemOffset") is not None:
        out["item_offset"] = data["itemOffset"]
    else:
        out["item_offset"] = 0
    if data.get("pageSize") is not None:
        out["page_size"] = data["pageSize"]
    if data.get("queueIds") is not None:
        import capo_deadline.types.queue_ids

        out["queue_ids"] = capo_deadline.types.queue_ids.deserialize_json(
            data["queueIds"]
        )
    else:
        out["queue_ids"] = []
    return out
