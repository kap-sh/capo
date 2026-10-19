"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceLevelTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.record_number
    import capo_lex_models_v2.types.test_set_conversation_id
    import capo_lex_models_v2.types.test_set_turn_result


class UtteranceLevelTestResultItem(TypedDict, closed=True):
    record_number: "capo_lex_models_v2.types.record_number.RecordNumber"
    """<p>The record number of the result.</p>"""
    conversation_id: NotRequired[
        "capo_lex_models_v2.types.test_set_conversation_id.TestSetConversationId"
    ]
    """<p>The unique identifier for the conversation associated with the result.</p>"""
    turn_result: "capo_lex_models_v2.types.test_set_turn_result.TestSetTurnResult"
    """<p>Contains information about the turn associated with the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceLevelTestResultItem) -> dict:
    out: dict = {}
    out["recordNumber"] = value["record_number"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    import capo_lex_models_v2.types.test_set_turn_result

    out["turnResult"] = capo_lex_models_v2.types.test_set_turn_result.serialize_json(
        value["turn_result"]
    )
    return out


def deserialize_json(data: dict) -> UtteranceLevelTestResultItem:
    out: UtteranceLevelTestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("recordNumber") is not None:
        out["record_number"] = data["recordNumber"]
    else:
        out["record_number"] = 0
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    if data.get("turnResult") is not None:
        import capo_lex_models_v2.types.test_set_turn_result

        out["turn_result"] = (
            capo_lex_models_v2.types.test_set_turn_result.deserialize_json(
                data["turnResult"]
            )
        )
    else:
        raise DeserializationError("UtteranceLevelTestResultItem.turn_result required")
    return out
