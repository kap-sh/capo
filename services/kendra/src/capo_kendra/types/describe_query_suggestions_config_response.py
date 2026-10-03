"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeQuerySuggestionsConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.attribute_suggestions_describe_config
    import capo_kendra.types.integer
    import capo_kendra.types.minimum_number_of_querying_users
    import capo_kendra.types.minimum_query_count
    import capo_kendra.types.mode
    import capo_kendra.types.object_boolean
    import capo_kendra.types.query_suggestions_status
    import capo_kendra.types.timestamp


class DescribeQuerySuggestionsConfigResponse(TypedDict, closed=True):
    mode: NotRequired["capo_kendra.types.mode.Mode"]
    """<p>Whether query suggestions are currently in <code>ENABLED</code> mode or <code>LEARN_ONLY</code> mode.</p> <p>By default, Amazon Kendra enables query suggestions.<code>LEARN_ONLY</code> turns off query suggestions for your users. You can change the mode using the <a href="https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html">UpdateQuerySuggestionsConfig</a> API.</p>"""
    status: NotRequired[
        "capo_kendra.types.query_suggestions_status.QuerySuggestionsStatus"
    ]
    """<p>Whether the status of query suggestions settings is currently <code>ACTIVE</code> or <code>UPDATING</code>.</p> <p>Active means the current settings apply and Updating means your changed settings are in the process of applying.</p>"""
    query_log_look_back_window_in_days: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>How recent your queries are in your query log time window (in days).</p>"""
    include_queries_without_user_information: NotRequired[
        "capo_kendra.types.object_boolean.ObjectBoolean"
    ]
    """<p> <code>TRUE</code> to use all queries, otherwise use only queries that include user information to generate the query suggestions.</p>"""
    minimum_number_of_querying_users: NotRequired[
        "capo_kendra.types.minimum_number_of_querying_users.MinimumNumberOfQueryingUsers"
    ]
    """<p>The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.</p>"""
    minimum_query_count: NotRequired[
        "capo_kendra.types.minimum_query_count.MinimumQueryCount"
    ]
    """<p>The minimum number of times a query must be searched in order for the query to be eligible to suggest to your users.</p>"""
    last_suggestions_build_time: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when query suggestions for an index was last updated.</p> <p>Amazon Kendra automatically updates suggestions every 24 hours, after you change a setting or after you apply a <a href="https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist">block list</a>.</p>"""
    last_clear_time: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when query suggestions for an index was last cleared.</p> <p>After you clear suggestions, Amazon Kendra learns new suggestions based on new queries added to the query log from the time you cleared suggestions. Amazon Kendra only considers re-occurences of a query from the time you cleared suggestions. </p>"""
    total_suggestions_count: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The current total count of query suggestions for an index.</p> <p>This count can change when you update your query suggestions settings, if you filter out certain queries from suggestions using a block list, and as the query log accumulates more queries for Amazon Kendra to learn from.</p> <p>If the count is much lower than you expected, it could be because Amazon Kendra needs more queries in the query history to learn from or your current query suggestions settings are too strict.</p>"""
    attribute_suggestions_config: NotRequired[
        "capo_kendra.types.attribute_suggestions_describe_config.AttributeSuggestionsDescribeConfig"
    ]
    """<p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQuerySuggestionsConfigResponse) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_kendra.types.mode

        out["Mode"] = capo_kendra.types.mode.serialize_aws_json_1_1(value["mode"])
    if "status" in value:
        import capo_kendra.types.query_suggestions_status

        out["Status"] = (
            capo_kendra.types.query_suggestions_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "query_log_look_back_window_in_days" in value:
        out["QueryLogLookBackWindowInDays"] = value[
            "query_log_look_back_window_in_days"
        ]
    if "include_queries_without_user_information" in value:
        out["IncludeQueriesWithoutUserInformation"] = value[
            "include_queries_without_user_information"
        ]
    if "minimum_number_of_querying_users" in value:
        out["MinimumNumberOfQueryingUsers"] = value["minimum_number_of_querying_users"]
    if "minimum_query_count" in value:
        out["MinimumQueryCount"] = value["minimum_query_count"]
    if "last_suggestions_build_time" in value:
        import capo_kendra.types.timestamp

        out["LastSuggestionsBuildTime"] = (
            capo_kendra.types.timestamp.serialize_aws_json_1_1(
                value["last_suggestions_build_time"]
            )
        )
    if "last_clear_time" in value:
        import capo_kendra.types.timestamp

        out["LastClearTime"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["last_clear_time"]
        )
    if "total_suggestions_count" in value:
        out["TotalSuggestionsCount"] = value["total_suggestions_count"]
    if "attribute_suggestions_config" in value:
        import capo_kendra.types.attribute_suggestions_describe_config

        out["AttributeSuggestionsConfig"] = (
            capo_kendra.types.attribute_suggestions_describe_config.serialize_aws_json_1_1(
                value["attribute_suggestions_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQuerySuggestionsConfigResponse:
    out: DescribeQuerySuggestionsConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_kendra.types.mode

        out["mode"] = capo_kendra.types.mode.deserialize_aws_json_1_1(data["Mode"])
    if data.get("Status") is not None:
        import capo_kendra.types.query_suggestions_status

        out["status"] = (
            capo_kendra.types.query_suggestions_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("QueryLogLookBackWindowInDays") is not None:
        out["query_log_look_back_window_in_days"] = data["QueryLogLookBackWindowInDays"]
    if data.get("IncludeQueriesWithoutUserInformation") is not None:
        out["include_queries_without_user_information"] = data[
            "IncludeQueriesWithoutUserInformation"
        ]
    if data.get("MinimumNumberOfQueryingUsers") is not None:
        out["minimum_number_of_querying_users"] = data["MinimumNumberOfQueryingUsers"]
    if data.get("MinimumQueryCount") is not None:
        out["minimum_query_count"] = data["MinimumQueryCount"]
    if data.get("LastSuggestionsBuildTime") is not None:
        import capo_kendra.types.timestamp

        out["last_suggestions_build_time"] = (
            capo_kendra.types.timestamp.deserialize_aws_json_1_1(
                data["LastSuggestionsBuildTime"]
            )
        )
    if data.get("LastClearTime") is not None:
        import capo_kendra.types.timestamp

        out["last_clear_time"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["LastClearTime"]
        )
    if data.get("TotalSuggestionsCount") is not None:
        out["total_suggestions_count"] = data["TotalSuggestionsCount"]
    if data.get("AttributeSuggestionsConfig") is not None:
        import capo_kendra.types.attribute_suggestions_describe_config

        out["attribute_suggestions_config"] = (
            capo_kendra.types.attribute_suggestions_describe_config.deserialize_aws_json_1_1(
                data["AttributeSuggestionsConfig"]
            )
        )
    return out
