"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListAggregatedUtterancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.aggregated_utterances_filters
    import capo_lex_models_v2.types.aggregated_utterances_sort_by
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.utterance_aggregation_duration


class ListAggregatedUtterancesRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot associated with this request.</p>"""
    bot_alias_id: NotRequired["capo_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the bot alias associated with this request. If you specify the bot alias, you can't specify the bot version.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The identifier of the bot version associated with this request. If you specify the bot version, you can't specify the bot alias.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale where the utterances were collected. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    aggregation_duration: "capo_lex_models_v2.types.utterance_aggregation_duration.UtteranceAggregationDuration"
    """<p>The time window for aggregating the utterance information. You can specify a time between one hour and two weeks.</p>"""
    sort_by: NotRequired[
        "capo_lex_models_v2.types.aggregated_utterances_sort_by.AggregatedUtterancesSortBy"
    ]
    """<p>Specifies sorting parameters for the list of utterances. You can sort by the hit count, the missed count, or the number of distinct sessions the utterance appeared in.</p>"""
    filters: NotRequired[
        "capo_lex_models_v2.types.aggregated_utterances_filters.AggregatedUtterancesFilters"
    ]
    """<p>Provides the specification of a filter used to limit the utterances in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of utterances to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. If you don't specify the <code>maxResults</code> parameter, 1,000 results are returned.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>If the response from the <code>ListAggregatedUtterances</code> operation contains more results that specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAggregatedUtterancesRequest) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    import capo_lex_models_v2.types.utterance_aggregation_duration

    out["aggregationDuration"] = (
        capo_lex_models_v2.types.utterance_aggregation_duration.serialize_json(
            value["aggregation_duration"]
        )
    )
    if "sort_by" in value:
        import capo_lex_models_v2.types.aggregated_utterances_sort_by

        out["sortBy"] = (
            capo_lex_models_v2.types.aggregated_utterances_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "filters" in value:
        import capo_lex_models_v2.types.aggregated_utterances_filters

        out["filters"] = (
            capo_lex_models_v2.types.aggregated_utterances_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAggregatedUtterancesRequest:
    out: ListAggregatedUtterancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("botAliasId") is not None:
        out["bot_alias_id"] = data["botAliasId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("ListAggregatedUtterancesRequest.locale_id required")
    if data.get("aggregationDuration") is not None:
        import capo_lex_models_v2.types.utterance_aggregation_duration

        out["aggregation_duration"] = (
            capo_lex_models_v2.types.utterance_aggregation_duration.deserialize_json(
                data["aggregationDuration"]
            )
        )
    else:
        raise DeserializationError(
            "ListAggregatedUtterancesRequest.aggregation_duration required"
        )
    if data.get("sortBy") is not None:
        import capo_lex_models_v2.types.aggregated_utterances_sort_by

        out["sort_by"] = (
            capo_lex_models_v2.types.aggregated_utterances_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if data.get("filters") is not None:
        import capo_lex_models_v2.types.aggregated_utterances_filters

        out["filters"] = (
            capo_lex_models_v2.types.aggregated_utterances_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
