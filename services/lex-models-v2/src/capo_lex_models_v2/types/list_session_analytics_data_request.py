"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListSessionAnalyticsDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_session_filters
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.session_data_sort_by
    import capo_lex_models_v2.types.timestamp


class ListSessionAnalyticsDataRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier for the bot for which you want to retrieve session analytics.</p>"""
    start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the beginning of the range of time for which you want to see session analytics.</p>"""
    end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>The date and time that marks the end of the range of time for which you want to see session analytics.</p>"""
    sort_by: NotRequired[
        "capo_lex_models_v2.types.session_data_sort_by.SessionDataSortBy"
    ]
    """<p>An object specifying the measure and method by which to sort the session analytics data.</p>"""
    filters: NotRequired[
        "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
    ]
    """<p>A list of objects, each of which describes a condition by which you want to filter the results.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionAnalyticsDataRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    if "sort_by" in value:
        import capo_lex_models_v2.types.session_data_sort_by

        out["sortBy"] = capo_lex_models_v2.types.session_data_sort_by.serialize_json(
            value["sort_by"]
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


def deserialize_json(data: dict) -> ListSessionAnalyticsDataRequest:
    out: ListSessionAnalyticsDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("startDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["start_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        import datetime

        out["start_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("endDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["end_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        import datetime

        out["end_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("sortBy") is not None:
        import capo_lex_models_v2.types.session_data_sort_by

        out["sort_by"] = capo_lex_models_v2.types.session_data_sort_by.deserialize_json(
            data["sortBy"]
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
