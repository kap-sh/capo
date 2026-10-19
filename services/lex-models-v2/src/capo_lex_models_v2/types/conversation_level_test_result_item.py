"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_level_intent_classification_results
    import capo_lex_models_v2.types.conversation_level_slot_resolution_results
    import capo_lex_models_v2.types.test_result_match_status
    import capo_lex_models_v2.types.test_set_conversation_id


class ConversationLevelTestResultItem(TypedDict, closed=True):
    conversation_id: (
        "capo_lex_models_v2.types.test_set_conversation_id.TestSetConversationId"
    )
    """<p>The conversation Id of the test result evaluation item.</p>"""
    end_to_end_result: (
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The end-to-end success or failure of the test result evaluation item.</p>"""
    speech_transcription_result: NotRequired[
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    ]
    """<p>The speech transcription success or failure of the test result evaluation item.</p>"""
    intent_classification_results: "capo_lex_models_v2.types.conversation_level_intent_classification_results.ConversationLevelIntentClassificationResults"
    """<p>The intent classification of the test result evaluation item.</p>"""
    slot_resolution_results: "capo_lex_models_v2.types.conversation_level_slot_resolution_results.ConversationLevelSlotResolutionResults"
    """<p>The slot success or failure of the test result evaluation item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResultItem) -> dict:
    out: dict = {}
    out["conversationId"] = value["conversation_id"]
    import capo_lex_models_v2.types.test_result_match_status

    out["endToEndResult"] = (
        capo_lex_models_v2.types.test_result_match_status.serialize_json(
            value["end_to_end_result"]
        )
    )
    if "speech_transcription_result" in value:
        import capo_lex_models_v2.types.test_result_match_status

        out["speechTranscriptionResult"] = (
            capo_lex_models_v2.types.test_result_match_status.serialize_json(
                value["speech_transcription_result"]
            )
        )
    import capo_lex_models_v2.types.conversation_level_intent_classification_results

    out["intentClassificationResults"] = (
        capo_lex_models_v2.types.conversation_level_intent_classification_results.serialize_json(
            value["intent_classification_results"]
        )
    )
    import capo_lex_models_v2.types.conversation_level_slot_resolution_results

    out["slotResolutionResults"] = (
        capo_lex_models_v2.types.conversation_level_slot_resolution_results.serialize_json(
            value["slot_resolution_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResultItem:
    out: ConversationLevelTestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    else:
        out["conversation_id"] = ""
    if data.get("endToEndResult") is not None:
        import capo_lex_models_v2.types.test_result_match_status

        out["end_to_end_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["endToEndResult"]
            )
        )
    else:
        import typing

        out["end_to_end_result"] = typing.cast(
            "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus",
            "",
        )
    if data.get("speechTranscriptionResult") is not None:
        import capo_lex_models_v2.types.test_result_match_status

        out["speech_transcription_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["speechTranscriptionResult"]
            )
        )
    if data.get("intentClassificationResults") is not None:
        import capo_lex_models_v2.types.conversation_level_intent_classification_results

        out["intent_classification_results"] = (
            capo_lex_models_v2.types.conversation_level_intent_classification_results.deserialize_json(
                data["intentClassificationResults"]
            )
        )
    else:
        out["intent_classification_results"] = []
    if data.get("slotResolutionResults") is not None:
        import capo_lex_models_v2.types.conversation_level_slot_resolution_results

        out["slot_resolution_results"] = (
            capo_lex_models_v2.types.conversation_level_slot_resolution_results.deserialize_json(
                data["slotResolutionResults"]
            )
        )
    else:
        out["slot_resolution_results"] = []
    return out
