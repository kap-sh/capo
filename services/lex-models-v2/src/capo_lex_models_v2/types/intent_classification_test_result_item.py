"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClassificationTestResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.intent_classification_test_result_item_counts
    import capo_lex_models_v2.types.name


class IntentClassificationTestResultItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent.</p>"""
    multi_turn_conversation: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether the conversation involves multiple turns or not.</p>"""
    result_counts: "capo_lex_models_v2.types.intent_classification_test_result_item_counts.IntentClassificationTestResultItemCounts"
    """<p>The result of the intent classification test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentClassificationTestResultItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["multiTurnConversation"] = value.get("multi_turn_conversation", False)
    import capo_lex_models_v2.types.intent_classification_test_result_item_counts

    out["resultCounts"] = (
        capo_lex_models_v2.types.intent_classification_test_result_item_counts.serialize_json(
            value["result_counts"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentClassificationTestResultItem:
    out: IntentClassificationTestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        out["intent_name"] = ""
    if data.get("multiTurnConversation") is not None:
        out["multi_turn_conversation"] = data["multiTurnConversation"]
    else:
        out["multi_turn_conversation"] = False
    if data.get("resultCounts") is not None:
        import capo_lex_models_v2.types.intent_classification_test_result_item_counts

        out["result_counts"] = (
            capo_lex_models_v2.types.intent_classification_test_result_item_counts.deserialize_json(
                data["resultCounts"]
            )
        )
    else:
        raise DeserializationError(
            "IntentClassificationTestResultItem.result_counts required"
        )
    return out
