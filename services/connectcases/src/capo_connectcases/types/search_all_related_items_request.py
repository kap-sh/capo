"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.next_token
    import capo_connectcases.types.related_item_filter_list
    import capo_connectcases.types.search_all_related_items_sort_list


class SearchAllRelatedItemsRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    filters: NotRequired[
        "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
    ]
    """<p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>"""
    sorts: NotRequired[
        "capo_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
    ]
    """<p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "sorts" in value:
        import capo_connectcases.types.search_all_related_items_sort_list

        out["sorts"] = (
            capo_connectcases.types.search_all_related_items_sort_list.serialize_json(
                value["sorts"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsRequest:
    out: SearchAllRelatedItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("sorts") is not None:
        import capo_connectcases.types.search_all_related_items_sort_list

        out["sorts"] = (
            capo_connectcases.types.search_all_related_items_sort_list.deserialize_json(
                data["sorts"]
            )
        )
    return out


def redact_sensitive(value: SearchAllRelatedItemsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_connectcases.types.related_item_filter_list

        out["filters"] = (
            capo_connectcases.types.related_item_filter_list.redact_sensitive(
                value["filters"]
            )
        )
    return out
