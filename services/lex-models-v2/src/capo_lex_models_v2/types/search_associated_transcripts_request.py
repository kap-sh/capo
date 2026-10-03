"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SearchAssociatedTranscriptsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.associated_transcript_filters
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_index
    import capo_lex_models_v2.types.search_order


class SearchAssociatedTranscriptsRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot associated with the transcripts that you are searching.</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot containing the transcripts that you are searching.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>"""
    bot_recommendation_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot recommendation associated with the transcripts to search.</p>"""
    search_order: NotRequired["capo_lex_models_v2.types.search_order.SearchOrder"]
    """<p>How SearchResults are ordered. Valid values are Ascending or Descending. The default is Descending.</p>"""
    filters: "capo_lex_models_v2.types.associated_transcript_filters.AssociatedTranscriptFilters"
    """<p>A list of filter objects.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>"""
    next_index: NotRequired["capo_lex_models_v2.types.next_index.NextIndex"]
    """<p>If the response from the SearchAssociatedTranscriptsRequest operation contains more results than specified in the maxResults parameter, an index is returned in the response. Use that index in the nextIndex parameter to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAssociatedTranscriptsRequest) -> dict:
    out: dict = {}
    if "search_order" in value:
        import capo_lex_models_v2.types.search_order

        out["searchOrder"] = capo_lex_models_v2.types.search_order.serialize_json(
            value["search_order"]
        )
    import capo_lex_models_v2.types.associated_transcript_filters

    out["filters"] = (
        capo_lex_models_v2.types.associated_transcript_filters.serialize_json(
            value["filters"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_index" in value:
        out["nextIndex"] = value["next_index"]
    return out


def deserialize_json(data: dict) -> SearchAssociatedTranscriptsRequest:
    out: SearchAssociatedTranscriptsRequest = {}  # type: ignore[typeddict-item]
    if data.get("searchOrder") is not None:
        import capo_lex_models_v2.types.search_order

        out["search_order"] = capo_lex_models_v2.types.search_order.deserialize_json(
            data["searchOrder"]
        )
    if data.get("filters") is not None:
        import capo_lex_models_v2.types.associated_transcript_filters

        out["filters"] = (
            capo_lex_models_v2.types.associated_transcript_filters.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError(
            "SearchAssociatedTranscriptsRequest.filters required"
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextIndex") is not None:
        out["next_index"] = data["nextIndex"]
    return out
