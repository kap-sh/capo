"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchCasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.next_token
    import capo_connectcases.types.search_cases_response_item_list
    import capo_connectcases.types.total_count


class SearchCasesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""
    cases: "capo_connectcases.types.search_cases_response_item_list.SearchCasesResponseItemList"
    """<p>A list of case documents where each case contains the properties <code>CaseId</code> and <code>Fields</code> where each field is a complex union structure. </p>"""
    total_count: "capo_connectcases.types.total_count.TotalCount"
    """<p>The total number of cases that matched the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchCasesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_connectcases.types.search_cases_response_item_list

    out["cases"] = (
        capo_connectcases.types.search_cases_response_item_list.serialize_json(
            value["cases"]
        )
    )
    out["totalCount"] = value.get("total_count", 0)
    return out


def deserialize_json(data: dict) -> SearchCasesResponse:
    out: SearchCasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cases") is not None:
        import capo_connectcases.types.search_cases_response_item_list

        out["cases"] = (
            capo_connectcases.types.search_cases_response_item_list.deserialize_json(
                data["cases"]
            )
        )
    else:
        out["cases"] = []
    if data.get("totalCount") is not None:
        out["total_count"] = data["totalCount"]
    else:
        out["total_count"] = 0
    return out
