"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotResolutionTestResultItemCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.count
    import capo_lex_models_v2.types.test_result_match_status_count_map


class SlotResolutionTestResultItemCounts(TypedDict, closed=True):
    total_result_count: "capo_lex_models_v2.types.count.Count"
    """<p>The total number of results.</p>"""
    speech_transcription_result_counts: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    ]
    """<p>The number of matched, mismatched and execution error results for speech transcription for the slot.</p>"""
    slot_match_result_counts: "capo_lex_models_v2.types.test_result_match_status_count_map.TestResultMatchStatusCountMap"
    """<p>The number of matched and mismatched results for slot resolution for the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotResolutionTestResultItemCounts) -> dict:
    out: dict = {}
    out["totalResultCount"] = value["total_result_count"]
    if "speech_transcription_result_counts" in value:
        import capo_lex_models_v2.types.test_result_match_status_count_map

        out["speechTranscriptionResultCounts"] = (
            capo_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
                value["speech_transcription_result_counts"]
            )
        )
    import capo_lex_models_v2.types.test_result_match_status_count_map

    out["slotMatchResultCounts"] = (
        capo_lex_models_v2.types.test_result_match_status_count_map.serialize_json(
            value["slot_match_result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotResolutionTestResultItemCounts:
    out: SlotResolutionTestResultItemCounts = {}  # type: ignore[typeddict-item]
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
    if data.get("slotMatchResultCounts") is not None:
        import capo_lex_models_v2.types.test_result_match_status_count_map

        out["slot_match_result_counts"] = (
            capo_lex_models_v2.types.test_result_match_status_count_map.deserialize_json(
                data["slotMatchResultCounts"]
            )
        )
    else:
        out["slot_match_result_counts"] = {}
    return out
