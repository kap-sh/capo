"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListChangeSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.filter_list
    import capo_marketplace_catalog.types.list_change_sets_max_result_integer
    import capo_marketplace_catalog.types.next_token
    import capo_marketplace_catalog.types.sort


class ListChangeSetsRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    filter_list: NotRequired["capo_marketplace_catalog.types.filter_list.FilterList"]
    """<p>An array of filter objects.</p>"""
    sort: NotRequired["capo_marketplace_catalog.types.sort.Sort"]
    """<p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>"""
    max_results: NotRequired[
        "capo_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
    ]
    """<p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangeSetsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "filter_list" in value:
        import capo_marketplace_catalog.types.filter_list

        out["FilterList"] = capo_marketplace_catalog.types.filter_list.serialize_json(
            value["filter_list"]
        )
    if "sort" in value:
        import capo_marketplace_catalog.types.sort

        out["Sort"] = capo_marketplace_catalog.types.sort.serialize_json(value["sort"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangeSetsRequest:
    out: ListChangeSetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("FilterList") is not None:
        import capo_marketplace_catalog.types.filter_list

        out["filter_list"] = (
            capo_marketplace_catalog.types.filter_list.deserialize_json(
                data["FilterList"]
            )
        )
    if data.get("Sort") is not None:
        import capo_marketplace_catalog.types.sort

        out["sort"] = capo_marketplace_catalog.types.sort.deserialize_json(data["Sort"])
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
