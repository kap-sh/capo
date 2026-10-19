"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SearchSampleQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.pagination_token
    import capo_cloudtrail.types.search_sample_queries_max_results
    import capo_cloudtrail.types.search_sample_queries_search_phrase


class SearchSampleQueriesRequest(TypedDict, closed=True):
    search_phrase: "capo_cloudtrail.types.search_sample_queries_search_phrase.SearchSampleQueriesSearchPhrase"
    """<p> The natural language phrase to use for the semantic search. The phrase must be in English. The length constraint is in characters, not words.</p>"""
    max_results: NotRequired[
        "capo_cloudtrail.types.search_sample_queries_max_results.SearchSampleQueriesMaxResults"
    ]
    """<p> The maximum number of results to return on a single page. The default value is 10. </p>"""
    next_token: NotRequired["capo_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of results. The length constraint is in characters, not words. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSampleQueriesRequest) -> dict:
    out: dict = {}
    out["SearchPhrase"] = value["search_phrase"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSampleQueriesRequest:
    out: SearchSampleQueriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SearchPhrase") is not None:
        out["search_phrase"] = data["SearchPhrase"]
    else:
        out["search_phrase"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
