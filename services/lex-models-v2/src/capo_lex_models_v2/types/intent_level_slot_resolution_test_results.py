"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentLevelSlotResolutionTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list


class IntentLevelSlotResolutionTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list.IntentLevelSlotResolutionTestResultItemList"
    """<p>Indicates the items for the slot level resolution for the intents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentLevelSlotResolutionTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentLevelSlotResolutionTestResults:
    out: IntentLevelSlotResolutionTestResults = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.intent_level_slot_resolution_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
