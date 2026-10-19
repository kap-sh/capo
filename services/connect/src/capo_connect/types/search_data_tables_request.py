"""Generated from Smithy shape ``com.amazonaws.connect#SearchDataTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_search_criteria
    import capo_connect.types.data_table_search_filter
    import capo_connect.types.instance_id
    import capo_connect.types.max_result1000
    import capo_connect.types.next_token


class SearchDataTablesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance to search within.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of data tables to return in one page of results.</p>"""
    search_filter: NotRequired[
        "capo_connect.types.data_table_search_filter.DataTableSearchFilter"
    ]
    """<p>Optional filters to apply to the search results, such as tag-based filtering for attribute-based access control.</p>"""
    search_criteria: NotRequired[
        "capo_connect.types.data_table_search_criteria.DataTableSearchCriteria"
    ]
    """<p>Search criteria including string conditions for matching table names, descriptions, or resource IDs. Supports STARTS_WITH, CONTAINS, and EXACT comparison types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataTablesRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_filter" in value:
        import capo_connect.types.data_table_search_filter

        out["SearchFilter"] = (
            capo_connect.types.data_table_search_filter.serialize_json(
                value["search_filter"]
            )
        )
    if "search_criteria" in value:
        import capo_connect.types.data_table_search_criteria

        out["SearchCriteria"] = (
            capo_connect.types.data_table_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchDataTablesRequest:
    out: SearchDataTablesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SearchFilter") is not None:
        import capo_connect.types.data_table_search_filter

        out["search_filter"] = (
            capo_connect.types.data_table_search_filter.deserialize_json(
                data["SearchFilter"]
            )
        )
    if data.get("SearchCriteria") is not None:
        import capo_connect.types.data_table_search_criteria

        out["search_criteria"] = (
            capo_connect.types.data_table_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    return out
