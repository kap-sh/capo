"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.max_results
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.search_filter_list
    import capo_marketplace_discovery.types.search_listings_sort_by
    import capo_marketplace_discovery.types.search_listings_sort_order
    import capo_marketplace_discovery.types.search_text


class SearchListingsInput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See <code>Locale</code> for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.</p>"""
    search_text: NotRequired["capo_marketplace_discovery.types.search_text.SearchText"]
    """<p>The search query text to find relevant listings.</p>"""
    filters: NotRequired[
        "capo_marketplace_discovery.types.search_filter_list.SearchFilterList"
    ]
    """<p>Filters to narrow search results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>"""
    max_results: NotRequired["capo_marketplace_discovery.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    sort_by: NotRequired[
        "capo_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
    ]
    """<p>The field to sort results by. Valid values are <code>RELEVANCE</code> and <code>AVERAGE_CUSTOMER_RATING</code>.</p>"""
    sort_order: NotRequired[
        "capo_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
    ]
    """<p>The sort direction. Valid values are <code>DESCENDING</code> and <code>ASCENDING</code>.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsInput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "filters" in value:
        import capo_marketplace_discovery.types.search_filter_list

        out["filters"] = (
            capo_marketplace_discovery.types.search_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_by" in value:
        import capo_marketplace_discovery.types.search_listings_sort_by

        out["sortBy"] = (
            capo_marketplace_discovery.types.search_listings_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_marketplace_discovery.types.search_listings_sort_order

        out["sortOrder"] = (
            capo_marketplace_discovery.types.search_listings_sort_order.serialize_json(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchListingsInput:
    out: SearchListingsInput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("searchText") is not None:
        out["search_text"] = data["searchText"]
    if data.get("filters") is not None:
        import capo_marketplace_discovery.types.search_filter_list

        out["filters"] = (
            capo_marketplace_discovery.types.search_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortBy") is not None:
        import capo_marketplace_discovery.types.search_listings_sort_by

        out["sort_by"] = (
            capo_marketplace_discovery.types.search_listings_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_marketplace_discovery.types.search_listings_sort_order

        out["sort_order"] = (
            capo_marketplace_discovery.types.search_listings_sort_order.deserialize_json(
                data["sortOrder"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
