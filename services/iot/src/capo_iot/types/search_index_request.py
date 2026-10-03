"""Generated from Smithy shape ``com.amazonaws.iot#SearchIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.index_name
    import capo_iot.types.next_token
    import capo_iot.types.query_string
    import capo_iot.types.query_version
    import capo_iot.types.search_query_max_results


class SearchIndexRequest(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The search index name.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The search query string. For more information about the search query syntax, see <a href="https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html">Query syntax</a>.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token used to get the next set of results, or <code>null</code> if there are no additional results.</p>"""
    max_results: NotRequired[
        "capo_iot.types.search_query_max_results.SearchQueryMaxResults"
    ]
    """<p>The maximum number of results to return per page at one time. This maximum number cannot exceed 100. The response might contain fewer results but will never contain more. You can use <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_SearchIndex.html#iot-SearchIndex-request-nextToken"> <code>nextToken</code> </a> to retrieve the next set of results until <code>nextToken</code> returns <code>NULL</code>.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The query version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchIndexRequest) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> SearchIndexRequest:
    out: SearchIndexRequest = {}  # type: ignore[typeddict-item]
    if data.get("indexName") is not None:
        out["index_name"] = data["indexName"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("SearchIndexRequest.query_string required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("queryVersion") is not None:
        out["query_version"] = data["queryVersion"]
    return out
