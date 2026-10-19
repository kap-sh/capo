"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.client_request_token
    import capo_timestream_query.types.max_query_results
    import capo_timestream_query.types.pagination_token
    import capo_timestream_query.types.query_insights
    import capo_timestream_query.types.query_string


class QueryRequest(TypedDict, closed=True):
    query_string: "capo_timestream_query.types.query_string.QueryString"
    """<p> The query to be run by Timestream. </p>"""
    client_token: NotRequired[
        "capo_timestream_query.types.client_request_token.ClientRequestToken"
    ]
    """<p> Unique, case-sensitive string of up to 64 ASCII characters specified when a <code>Query</code> request is made. Providing a <code>ClientToken</code> makes the call to <code>Query</code> <i>idempotent</i>. This means that running the same query repeatedly will produce the same result. In other words, making multiple identical <code>Query</code> requests has the same effect as making a single request. When using <code>ClientToken</code> in a query, note the following: </p> <ul> <li> <p> If the Query API is instantiated without a <code>ClientToken</code>, the Query SDK generates a <code>ClientToken</code> on your behalf.</p> </li> <li> <p>If the <code>Query</code> invocation only contains the <code>ClientToken</code> but does not include a <code>NextToken</code>, that invocation of <code>Query</code> is assumed to be a new query run.</p> </li> <li> <p>If the invocation contains <code>NextToken</code>, that particular invocation is assumed to be a subsequent invocation of a prior call to the Query API, and a result set is returned.</p> </li> <li> <p> After 4 hours, any request with the same <code>ClientToken</code> is treated as a new request. </p> </li> </ul>"""
    next_token: NotRequired[
        "capo_timestream_query.types.pagination_token.PaginationToken"
    ]
    """<p> A pagination token used to return a set of results. When the <code>Query</code> API is invoked using <code>NextToken</code>, that particular invocation is assumed to be a subsequent invocation of a prior call to <code>Query</code>, and a result set is returned. However, if the <code>Query</code> invocation only contains the <code>ClientToken</code>, that invocation of <code>Query</code> is assumed to be a new query run. </p> <p>Note the following when using NextToken in a query:</p> <ul> <li> <p>A pagination token can be used for up to five <code>Query</code> invocations, OR for a duration of up to 1 hour – whichever comes first.</p> </li> <li> <p>Using the same <code>NextToken</code> will return the same set of records. To keep paginating through the result set, you must to use the most recent <code>nextToken</code>.</p> </li> <li> <p>Suppose a <code>Query</code> invocation returns two <code>NextToken</code> values, <code>TokenA</code> and <code>TokenB</code>. If <code>TokenB</code> is used in a subsequent <code>Query</code> invocation, then <code>TokenA</code> is invalidated and cannot be reused.</p> </li> <li> <p>To request a previous result set from a query after pagination has begun, you must re-invoke the Query API.</p> </li> <li> <p>The latest <code>NextToken</code> should be used to paginate until <code>null</code> is returned, at which point a new <code>NextToken</code> should be used.</p> </li> <li> <p> If the IAM principal of the query initiator and the result reader are not the same and/or the query initiator and the result reader do not have the same query string in the query requests, the query will fail with an <code>Invalid pagination token</code> error. </p> </li> </ul>"""
    max_rows: NotRequired[
        "capo_timestream_query.types.max_query_results.MaxQueryResults"
    ]
    """<p> The total number of rows to be returned in the <code>Query</code> output. The initial run of <code>Query</code> with a <code>MaxRows</code> value specified will return the result set of the query in two cases: </p> <ul> <li> <p>The size of the result is less than <code>1MB</code>.</p> </li> <li> <p>The number of rows in the result set is less than the value of <code>maxRows</code>.</p> </li> </ul> <p>Otherwise, the initial invocation of <code>Query</code> only returns a <code>NextToken</code>, which can then be used in subsequent calls to fetch the result set. To resume pagination, provide the <code>NextToken</code> value in the subsequent command.</p> <p>If the row size is large (e.g. a row has many columns), Timestream may return fewer rows to keep the response size from exceeding the 1 MB limit. If <code>MaxRows</code> is not provided, Timestream will send the necessary number of rows to meet the 1 MB limit.</p>"""
    query_insights: NotRequired[
        "capo_timestream_query.types.query_insights.QueryInsights"
    ]
    """<p>Encapsulates settings for enabling <code>QueryInsights</code>.</p> <p>Enabling <code>QueryInsights</code> returns insights and metrics in addition to query results for the query that you executed. You can use <code>QueryInsights</code> to tune your query performance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryRequest) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_rows" in value:
        out["MaxRows"] = value["max_rows"]
    if "query_insights" in value:
        import capo_timestream_query.types.query_insights

        out["QueryInsights"] = (
            capo_timestream_query.types.query_insights.serialize_aws_json_1_0(
                value["query_insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryRequest:
    out: QueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    else:
        out["query_string"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxRows") is not None:
        out["max_rows"] = data["MaxRows"]
    if data.get("QueryInsights") is not None:
        import capo_timestream_query.types.query_insights

        out["query_insights"] = (
            capo_timestream_query.types.query_insights.deserialize_aws_json_1_0(
                data["QueryInsights"]
            )
        )
    return out


def redact_sensitive(value: QueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_string" in value:
        out["query_string"] = "*** Sensitive Data Redacted ***"
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
