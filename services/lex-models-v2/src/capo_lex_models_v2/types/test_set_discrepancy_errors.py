"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyErrors``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_set_intent_discrepancy_list
    import capo_lex_models_v2.types.test_set_slot_discrepancy_list


class TestSetDiscrepancyErrors(TypedDict, closed=True):
    intent_discrepancies: "capo_lex_models_v2.types.test_set_intent_discrepancy_list.TestSetIntentDiscrepancyList"
    """<p>Contains information about discrepancies found for intents between the test set and the bot.</p>"""
    slot_discrepancies: "capo_lex_models_v2.types.test_set_slot_discrepancy_list.TestSetSlotDiscrepancyList"
    """<p>Contains information about discrepancies found for slots between the test set and the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyErrors) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.test_set_intent_discrepancy_list

    out["intentDiscrepancies"] = (
        capo_lex_models_v2.types.test_set_intent_discrepancy_list.serialize_json(
            value["intent_discrepancies"]
        )
    )
    import capo_lex_models_v2.types.test_set_slot_discrepancy_list

    out["slotDiscrepancies"] = (
        capo_lex_models_v2.types.test_set_slot_discrepancy_list.serialize_json(
            value["slot_discrepancies"]
        )
    )
    return out


def deserialize_json(data: dict) -> TestSetDiscrepancyErrors:
    out: TestSetDiscrepancyErrors = {}  # type: ignore[typeddict-item]
    if data.get("intentDiscrepancies") is not None:
        import capo_lex_models_v2.types.test_set_intent_discrepancy_list

        out["intent_discrepancies"] = (
            capo_lex_models_v2.types.test_set_intent_discrepancy_list.deserialize_json(
                data["intentDiscrepancies"]
            )
        )
    else:
        out["intent_discrepancies"] = []
    if data.get("slotDiscrepancies") is not None:
        import capo_lex_models_v2.types.test_set_slot_discrepancy_list

        out["slot_discrepancies"] = (
            capo_lex_models_v2.types.test_set_slot_discrepancy_list.deserialize_json(
                data["slotDiscrepancies"]
            )
        )
    else:
        out["slot_discrepancies"] = []
    return out
