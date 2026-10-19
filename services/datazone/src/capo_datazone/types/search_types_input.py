"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.filter_clause
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.search_in_list
    import capo_datazone.types.search_sort
    import capo_datazone.types.search_text
    import capo_datazone.types.types_search_scope


class SearchTypesInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which to invoke the <code>SearchTypes</code> action.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call to <code>SearchTypes</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchTypes</code> to list the next set of results. </p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchTypes</code> to list the next set of results.</p>"""
    search_scope: "capo_datazone.types.types_search_scope.TypesSearchScope"
    """<p>Specifies the scope of the search for types.</p>"""
    search_text: NotRequired["capo_datazone.types.search_text.SearchText"]
    """<p>Specifies the text for which to search.</p>"""
    search_in: NotRequired["capo_datazone.types.search_in_list.SearchInList"]
    """<p>The details of the search.</p>"""
    filters: NotRequired["capo_datazone.types.filter_clause.FilterClause"]
    """<p>The filters for the <code>SearchTypes</code> action.</p>"""
    sort: NotRequired["capo_datazone.types.search_sort.SearchSort"]
    """<p>The specifies the way to sort the <code>SearchTypes</code> results.</p>"""
    managed: "bool"
    """<p>Specifies whether the search is managed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_datazone.types.types_search_scope

    out["searchScope"] = capo_datazone.types.types_search_scope.serialize_json(
        value["search_scope"]
    )
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "search_in" in value:
        import capo_datazone.types.search_in_list

        out["searchIn"] = capo_datazone.types.search_in_list.serialize_json(
            value["search_in"]
        )
    if "filters" in value:
        import capo_datazone.types.filter_clause

        out["filters"] = capo_datazone.types.filter_clause.serialize_json(
            value["filters"]
        )
    if "sort" in value:
        import capo_datazone.types.search_sort

        out["sort"] = capo_datazone.types.search_sort.serialize_json(value["sort"])
    out["managed"] = value["managed"]
    return out


def deserialize_json(data: dict) -> SearchTypesInput:
    out: SearchTypesInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("searchScope") is not None:
        import capo_datazone.types.types_search_scope

        out["search_scope"] = capo_datazone.types.types_search_scope.deserialize_json(
            data["searchScope"]
        )
    else:
        import typing

        out["search_scope"] = typing.cast(
            "capo_datazone.types.types_search_scope.TypesSearchScope", ""
        )
    if data.get("searchText") is not None:
        out["search_text"] = data["searchText"]
    if data.get("searchIn") is not None:
        import capo_datazone.types.search_in_list

        out["search_in"] = capo_datazone.types.search_in_list.deserialize_json(
            data["searchIn"]
        )
    if data.get("filters") is not None:
        import capo_datazone.types.filter_clause

        out["filters"] = capo_datazone.types.filter_clause.deserialize_json(
            data["filters"]
        )
    if data.get("sort") is not None:
        import capo_datazone.types.search_sort

        out["sort"] = capo_datazone.types.search_sort.deserialize_json(data["sort"])
    if data.get("managed") is not None:
        out["managed"] = data["managed"]
    else:
        out["managed"] = False
    return out
