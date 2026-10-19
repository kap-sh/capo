"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateQuerySuggestionsConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.attribute_suggestions_update_config
    import capo_kendra.types.index_id
    import capo_kendra.types.integer
    import capo_kendra.types.minimum_number_of_querying_users
    import capo_kendra.types.minimum_query_count
    import capo_kendra.types.mode
    import capo_kendra.types.object_boolean


class UpdateQuerySuggestionsConfigRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p> The identifier of the index with query suggestions you want to update.</p>"""
    mode: NotRequired["capo_kendra.types.mode.Mode"]
    """<p>Set the mode to <code>ENABLED</code> or <code>LEARN_ONLY</code>.</p> <p>By default, Amazon Kendra enables query suggestions. <code>LEARN_ONLY</code> mode allows you to turn off query suggestions. You can to update this at any time.</p> <p>In <code>LEARN_ONLY</code> mode, Amazon Kendra continues to learn from new queries to keep suggestions up to date for when you are ready to switch to ENABLED mode again.</p>"""
    query_log_look_back_window_in_days: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>How recent your queries are in your query log time window.</p> <p>The time window is the number of days from current day to past days.</p> <p>By default, Amazon Kendra sets this to 180.</p>"""
    include_queries_without_user_information: NotRequired[
        "capo_kendra.types.object_boolean.ObjectBoolean"
    ]
    """<p> <code>TRUE</code> to include queries without user information (i.e. all queries, irrespective of the user), otherwise <code>FALSE</code> to only include queries with user information.</p> <p>If you pass user information to Amazon Kendra along with the queries, you can set this flag to <code>FALSE</code> and instruct Amazon Kendra to only consider queries with user information.</p> <p>If you set to <code>FALSE</code>, Amazon Kendra only considers queries searched at least <code>MinimumQueryCount</code> times across <code>MinimumNumberOfQueryingUsers</code> unique users for suggestions.</p> <p>If you set to <code>TRUE</code>, Amazon Kendra ignores all user information and learns from all queries.</p>"""
    minimum_number_of_querying_users: NotRequired[
        "capo_kendra.types.minimum_number_of_querying_users.MinimumNumberOfQueryingUsers"
    ]
    """<p>The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.</p> <p>Increasing this number might decrease the number of suggestions. However, this ensures a query is searched by many users and is truly popular to suggest to users.</p> <p>How you tune this setting depends on your specific needs.</p>"""
    minimum_query_count: NotRequired[
        "capo_kendra.types.minimum_query_count.MinimumQueryCount"
    ]
    """<p>The the minimum number of times a query must be searched in order to be eligible to suggest to your users.</p> <p>Decreasing this number increases the number of suggestions. However, this affects the quality of suggestions as it sets a low bar for a query to be considered popular to suggest to users.</p> <p>How you tune this setting depends on your specific needs.</p>"""
    attribute_suggestions_config: NotRequired[
        "capo_kendra.types.attribute_suggestions_update_config.AttributeSuggestionsUpdateConfig"
    ]
    """<p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQuerySuggestionsConfigRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "mode" in value:
        import capo_kendra.types.mode

        out["Mode"] = capo_kendra.types.mode.serialize_aws_json_1_1(value["mode"])
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
    if "attribute_suggestions_config" in value:
        import capo_kendra.types.attribute_suggestions_update_config

        out["AttributeSuggestionsConfig"] = (
            capo_kendra.types.attribute_suggestions_update_config.serialize_aws_json_1_1(
                value["attribute_suggestions_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQuerySuggestionsConfigRequest:
    out: UpdateQuerySuggestionsConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("Mode") is not None:
        import capo_kendra.types.mode

        out["mode"] = capo_kendra.types.mode.deserialize_aws_json_1_1(data["Mode"])
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
    if data.get("AttributeSuggestionsConfig") is not None:
        import capo_kendra.types.attribute_suggestions_update_config

        out["attribute_suggestions_config"] = (
            capo_kendra.types.attribute_suggestions_update_config.deserialize_aws_json_1_1(
                data["AttributeSuggestionsConfig"]
            )
        )
    return out
