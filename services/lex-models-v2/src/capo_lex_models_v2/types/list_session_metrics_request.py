"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListSessionMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_bin_by_list
    import capo_lex_models_v2.types.analytics_session_filters
    import capo_lex_models_v2.types.analytics_session_group_by_list
    import capo_lex_models_v2.types.analytics_session_metrics
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.timestamp


class ListSessionMetricsRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier for the bot for which you want to retrieve session metrics.</p>"""
    start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the beginning of the range of time for which you want to see session metrics.</p>"""
    end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the end of the range of time for which you want to see session metrics.</p>"""
    metrics: (
        "capo_lex_models_v2.types.analytics_session_metrics.AnalyticsSessionMetrics"
    )
    """<p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>"""
    bin_by: NotRequired[
        "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
    ]
    """<p>A list of objects, each of which contains specifications for organizing the results by time.</p>"""
    group_by: NotRequired[
        "capo_lex_models_v2.types.analytics_session_group_by_list.AnalyticsSessionGroupByList"
    ]
    """<p>A list of objects, each of which specifies how to group the results. You can group by the following criteria:</p> <ul> <li> <p> <code>ConversationEndState</code> – The final state of the conversation. The possible end states are detailed in <a href="https://docs.aws.amazon.com/analytics-key-definitions-conversations">Key definitions</a> in the user guide.</p> </li> <li> <p> <code>LocaleId</code> – The unique identifier of the bot locale.</p> </li> </ul>"""
    filters: NotRequired[
        "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
    ]
    """<p>A list of objects, each of which describes a condition by which you want to filter the results.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListSessionMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionMetrics request to return the next page of results. For a complete set of results, call the ListSessionMetrics operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionMetricsRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    import capo_lex_models_v2.types.analytics_session_metrics

    out["metrics"] = capo_lex_models_v2.types.analytics_session_metrics.serialize_json(
        value["metrics"]
    )
    if "bin_by" in value:
        import capo_lex_models_v2.types.analytics_bin_by_list

        out["binBy"] = capo_lex_models_v2.types.analytics_bin_by_list.serialize_json(
            value["bin_by"]
        )
    if "group_by" in value:
        import capo_lex_models_v2.types.analytics_session_group_by_list

        out["groupBy"] = (
            capo_lex_models_v2.types.analytics_session_group_by_list.serialize_json(
                value["group_by"]
            )
        )
    if "filters" in value:
        import capo_lex_models_v2.types.analytics_session_filters

        out["filters"] = (
            capo_lex_models_v2.types.analytics_session_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionMetricsRequest:
    out: ListSessionMetricsRequest = {}  # type: ignore[typeddict-item]
    if data.get("startDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["start_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        raise DeserializationError("ListSessionMetricsRequest.start_date_time required")
    if data.get("endDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["end_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        raise DeserializationError("ListSessionMetricsRequest.end_date_time required")
    if data.get("metrics") is not None:
        import capo_lex_models_v2.types.analytics_session_metrics

        out["metrics"] = (
            capo_lex_models_v2.types.analytics_session_metrics.deserialize_json(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("ListSessionMetricsRequest.metrics required")
    if data.get("binBy") is not None:
        import capo_lex_models_v2.types.analytics_bin_by_list

        out["bin_by"] = capo_lex_models_v2.types.analytics_bin_by_list.deserialize_json(
            data["binBy"]
        )
    if data.get("groupBy") is not None:
        import capo_lex_models_v2.types.analytics_session_group_by_list

        out["group_by"] = (
            capo_lex_models_v2.types.analytics_session_group_by_list.deserialize_json(
                data["groupBy"]
            )
        )
    if data.get("filters") is not None:
        import capo_lex_models_v2.types.analytics_session_filters

        out["filters"] = (
            capo_lex_models_v2.types.analytics_session_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
