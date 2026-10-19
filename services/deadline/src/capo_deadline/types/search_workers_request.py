"""Generated from Smithy shape ``com.amazonaws.deadline#SearchWorkersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_ids
    import capo_deadline.types.integer
    import capo_deadline.types.search_grouped_filter_expressions
    import capo_deadline.types.search_sort_expressions


class SearchWorkersRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID in the workers search.</p>"""
    filter_expressions: NotRequired[
        "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    sort_expressions: NotRequired[
        "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
    ]
    """<p>The search terms for a resource.</p>"""
    item_offset: "capo_deadline.types.integer.Integer"
    """<p>The offset for the search results.</p>"""
    page_size: NotRequired["capo_deadline.types.integer.Integer"]
    """<p>Specifies the number of results to return.</p>"""
    fleet_ids: "capo_deadline.types.fleet_ids.FleetIds"
    """<p>The fleet ID of the workers to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchWorkersRequest) -> dict:
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
    import capo_deadline.types.fleet_ids

    out["fleetIds"] = capo_deadline.types.fleet_ids.serialize_json(value["fleet_ids"])
    return out


def deserialize_json(data: dict) -> SearchWorkersRequest:
    out: SearchWorkersRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("SearchWorkersRequest.item_offset required")
    if data.get("pageSize") is not None:
        out["page_size"] = data["pageSize"]
    if data.get("fleetIds") is not None:
        import capo_deadline.types.fleet_ids

        out["fleet_ids"] = capo_deadline.types.fleet_ids.deserialize_json(
            data["fleetIds"]
        )
    else:
        raise DeserializationError("SearchWorkersRequest.fleet_ids required")
    return out
