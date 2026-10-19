"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OverallTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.count
    import capo_lex_models_v2.types.test_result_match_status_count_map


class OverallTestResultItem(TypedDict, closed=True):
    multi_turn_conversation: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether the conversation contains multiple turns or not.</p>"""
    total_result_count: "capo_lex_models_v2.types.count.Count"
    """<p>The total number of overall results in the result of the test execution.</p>"""
    speech_transcription_result_counts: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    ]
    """<p>The number of speech transcription results in the overall test.</p>"""
    end_to_end_result_counts: "capo_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    """<p>The number of results that succeeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverallTestResultItem) -> dict:
    out: dict = {}
    out["multiTurnConversation"] = value.get("multi_turn_conversation", False)
    out["totalResultCount"] = value["total_result_count"]
    if "speech_transcription_result_counts" in value:
        import capo_lex_models_v2.types.test_result_match_status_count_map

        out["speechTranscriptionResultCounts"] = (
            capo_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
                value["speech_transcription_result_counts"]
            )
        )
    import capo_lex_models_v2.types.test_result_match_status_count_map

    out["endToEndResultCounts"] = (
        capo_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
            value["end_to_end_result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> OverallTestResultItem:
    out: OverallTestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("multiTurnConversation") is not None:
        out["multi_turn_conversation"] = data["multiTurnConversation"]
    else:
        out["multi_turn_conversation"] = False
    if data.get("totalResultCount") is not None:
        out["total_result_count"] = data["totalResultCount"]
    else:
        out["total_result_count"] = 0
    if data.get("speechTranscriptionResultCounts") is not None:
        import capo_lex_models_v2.types.test_result_match_status_count_map

        out["speech_transcription_result_counts"] = (
            capo_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["speechTranscriptionResultCounts"]
            )
        )
    if data.get("endToEndResultCounts") is not None:
        import capo_lex_models_v2.types.test_result_match_status_count_map

        out["end_to_end_result_counts"] = (
            capo_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["endToEndResultCounts"]
            )
        )
    else:
        out["end_to_end_result_counts"] = {}
    return out
