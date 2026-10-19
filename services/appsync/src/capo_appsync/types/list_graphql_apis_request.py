"""Generated from Smithy shape ``com.amazonaws.appsync#ListGraphqlApisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.graph_ql_api_type
    import capo_appsync.types.max_results
    import capo_appsync.types.ownership
    import capo_appsync.types.pagination_token


class ListGraphqlApisRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""
    max_results: NotRequired["capo_appsync.types.max_results.MaxResults"]
    """<p>The maximum number of results that you want the request to return.</p>"""
    api_type: NotRequired["capo_appsync.types.graph_ql_api_type.GraphQLApiType"]
    """<p>The value that indicates whether the GraphQL API is a standard API (<code>GRAPHQL</code>) or merged API (<code>MERGED</code>).</p>"""
    owner: NotRequired["capo_appsync.types.ownership.Ownership"]
    """<p>The account owner of the GraphQL API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphqlApisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGraphqlApisRequest:
    out: ListGraphqlApisRequest = {}  # type: ignore[typeddict-item]
    return out
