"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSlotDiscrepancyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.string


class TestSetSlotDiscrepancyItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent associated with the slot in the discrepancy report.</p>"""
    slot_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the slot in the discrepancy report.</p>"""
    error_message: "capo_lex_models_v2.types.string.String"
    """<p>The error message for a discrepancy for an intent between the test set and the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSlotDiscrepancyItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["slotName"] = value["slot_name"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> TestSetSlotDiscrepancyItem:
    out: TestSetSlotDiscrepancyItem = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        out["intent_name"] = ""
    if data.get("slotName") is not None:
        out["slot_name"] = data["slotName"]
    else:
        out["slot_name"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
