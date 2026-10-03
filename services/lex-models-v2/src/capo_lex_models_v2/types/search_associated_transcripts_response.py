"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SearchAssociatedTranscriptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.associated_transcript_list
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_index


class SearchAssociatedTranscriptsResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot associated with the transcripts that you are searching.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot containing the transcripts that you are searching.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>"""
    bot_recommendation_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p> The unique identifier of the bot recommendation associated with the transcripts to search.</p>"""
    next_index: NotRequired["capo_lex_models_v2.types.next_index.NextIndex"]
    """<p>A index that indicates whether there are more results to return in a response to the SearchAssociatedTranscripts operation. If the nextIndex field is present, you send the contents as the nextIndex parameter of a SearchAssociatedTranscriptsRequest operation to get the next page of results.</p>"""
    associated_transcripts: NotRequired[
        "capo_lex_models_v2.types.associated_transcript_list.AssociatedTranscriptList"
    ]
    """<p>The object that contains the associated transcript that meet the criteria you specified.</p>"""
    total_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The total number of transcripts returned by the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAssociatedTranscriptsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_recommendation_id" in value:
        out["botRecommendationId"] = value["bot_recommendation_id"]
    if "next_index" in value:
        out["nextIndex"] = value["next_index"]
    if "associated_transcripts" in value:
        import capo_lex_models_v2.types.associated_transcript_list

        out["associatedTranscripts"] = (
            capo_lex_models_v2.types.associated_transcript_list.serialize_json(
                value["associated_transcripts"]
            )
        )
    if "total_results" in value:
        out["totalResults"] = value["total_results"]
    return out


def deserialize_json(data: dict) -> SearchAssociatedTranscriptsResponse:
    out: SearchAssociatedTranscriptsResponse = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("botRecommendationId") is not None:
        out["bot_recommendation_id"] = data["botRecommendationId"]
    if data.get("nextIndex") is not None:
        out["next_index"] = data["nextIndex"]
    if data.get("associatedTranscripts") is not None:
        import capo_lex_models_v2.types.associated_transcript_list

        out["associated_transcripts"] = (
            capo_lex_models_v2.types.associated_transcript_list.deserialize_json(
                data["associatedTranscripts"]
            )
        )
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    return out
