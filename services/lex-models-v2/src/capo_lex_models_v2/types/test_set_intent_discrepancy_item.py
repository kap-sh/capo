"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetIntentDiscrepancyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.string


class TestSetIntentDiscrepancyItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The name of the intent in the discrepancy report.</p>"""
    error_message: "capo_lex_models_v2.types.string.String"
    """<p>The error message for a discrepancy for an intent between the test set and the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetIntentDiscrepancyItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> TestSetIntentDiscrepancyItem:
    out: TestSetIntentDiscrepancyItem = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        out["intent_name"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
