"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.column_info_list
    import capo_timestream_query.types.pagination_token
    import capo_timestream_query.types.query_id
    import capo_timestream_query.types.query_insights_response
    import capo_timestream_query.types.query_status
    import capo_timestream_query.types.row_list


class QueryResponse(TypedDict, closed=True):
    query_id: "capo_timestream_query.types.query_id.QueryId"
    """<p> A unique ID for the given query. </p>"""
    next_token: NotRequired[
        "capo_timestream_query.types.pagination_token.PaginationToken"
    ]
    """<p> A pagination token that can be used again on a <code>Query</code> call to get the next set of results. </p>"""
    rows: "capo_timestream_query.types.row_list.RowList"
    """<p> The result set rows returned by the query. </p>"""
    column_info: "capo_timestream_query.types.column_info_list.ColumnInfoList"
    """<p> The column data types of the returned result set. </p>"""
    query_status: NotRequired["capo_timestream_query.types.query_status.QueryStatus"]
    """<p>Information about the status of the query, including progress and bytes scanned.</p>"""
    query_insights_response: NotRequired[
        "capo_timestream_query.types.query_insights_response.QueryInsightsResponse"
    ]
    """<p>Encapsulates <code>QueryInsights</code> containing insights and metrics related to the query that you executed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryResponse) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_timestream_query.types.row_list

    out["Rows"] = capo_timestream_query.types.row_list.serialize_aws_json_1_0(
        value["rows"]
    )
    import capo_timestream_query.types.column_info_list

    out["ColumnInfo"] = (
        capo_timestream_query.types.column_info_list.serialize_aws_json_1_0(
            value["column_info"]
        )
    )
    if "query_status" in value:
        import capo_timestream_query.types.query_status

        out["QueryStatus"] = (
            capo_timestream_query.types.query_status.serialize_aws_json_1_0(
                value["query_status"]
            )
        )
    if "query_insights_response" in value:
        import capo_timestream_query.types.query_insights_response

        out["QueryInsightsResponse"] = (
            capo_timestream_query.types.query_insights_response.serialize_aws_json_1_0(
                value["query_insights_response"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryResponse:
    out: QueryResponse = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Rows") is not None:
        import capo_timestream_query.types.row_list

        out["rows"] = capo_timestream_query.types.row_list.deserialize_aws_json_1_0(
            data["Rows"]
        )
    else:
        out["rows"] = []
    if data.get("ColumnInfo") is not None:
        import capo_timestream_query.types.column_info_list

        out["column_info"] = (
            capo_timestream_query.types.column_info_list.deserialize_aws_json_1_0(
                data["ColumnInfo"]
            )
        )
    else:
        out["column_info"] = []
    if data.get("QueryStatus") is not None:
        import capo_timestream_query.types.query_status

        out["query_status"] = (
            capo_timestream_query.types.query_status.deserialize_aws_json_1_0(
                data["QueryStatus"]
            )
        )
    if data.get("QueryInsightsResponse") is not None:
        import capo_timestream_query.types.query_insights_response

        out["query_insights_response"] = (
            capo_timestream_query.types.query_insights_response.deserialize_aws_json_1_0(
                data["QueryInsightsResponse"]
            )
        )
    return out
