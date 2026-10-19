"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetTurnRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.record_number
    import capo_lex_models_v2.types.test_set_conversation_id
    import capo_lex_models_v2.types.turn_number
    import capo_lex_models_v2.types.turn_specification


class TestSetTurnRecord(TypedDict, closed=True):
    record_number: "capo_lex_models_v2.types.record_number.RecordNumber"
    """<p>The record number associated with the turn.</p>"""
    conversation_id: NotRequired[
        "capo_lex_models_v2.types.test_set_conversation_id.TestSetConversationId"
    ]
    """<p>The unique identifier for the conversation associated with the turn.</p>"""
    turn_number: NotRequired["capo_lex_models_v2.types.turn_number.TurnNumber"]
    """<p>The number of turns that has elapsed up to that turn.</p>"""
    turn_specification: "capo_lex_models_v2.types.turn_specification.TurnSpecification"
    """<p>Contains information about the agent or user turn depending upon type of turn.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetTurnRecord) -> dict:
    out: dict = {}
    out["recordNumber"] = value["record_number"]
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "turn_number" in value:
        out["turnNumber"] = value["turn_number"]
    import capo_lex_models_v2.types.turn_specification

    out["turnSpecification"] = (
        capo_lex_models_v2.types.turn_specification.serialize_json(
            value["turn_specification"]
        )
    )
    return out


def deserialize_json(data: dict) -> TestSetTurnRecord:
    out: TestSetTurnRecord = {}  # type: ignore[typeddict-item]
    if data.get("recordNumber") is not None:
        out["record_number"] = data["recordNumber"]
    else:
        out["record_number"] = 0
    if data.get("conversationId") is not None:
        out["conversation_id"] = data["conversationId"]
    if data.get("turnNumber") is not None:
        out["turn_number"] = data["turnNumber"]
    if data.get("turnSpecification") is not None:
        import capo_lex_models_v2.types.turn_specification

        out["turn_specification"] = (
            capo_lex_models_v2.types.turn_specification.deserialize_json(
                data["turnSpecification"]
            )
        )
    else:
        raise DeserializationError("TestSetTurnRecord.turn_specification required")
    return out
