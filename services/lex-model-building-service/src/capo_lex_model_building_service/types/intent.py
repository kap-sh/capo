"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Intent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.intent_name
    import capo_lex_model_building_service.types.version


class Intent(TypedDict, closed=True):
    intent_name: "capo_lex_model_building_service.types.intent_name.IntentName"
    """<p>The name of the intent.</p>"""
    intent_version: "capo_lex_model_building_service.types.version.Version"
    """<p>The version of the intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Intent) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    out["intentVersion"] = value["intent_version"]
    return out


def deserialize_json(data: dict) -> Intent:
    out: Intent = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        out["intent_name"] = ""
    if data.get("intentVersion") is not None:
        out["intent_version"] = data["intentVersion"]
    else:
        out["intent_version"] = ""
    return out
