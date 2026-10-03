"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotDefaultValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_default_value_string


class SlotDefaultValue(TypedDict, closed=True):
    default_value: "capo_lex_model_building_service.types.slot_default_value_string.SlotDefaultValueString"
    """<p>The default value for the slot. You can specify one of the following:</p> <ul> <li> <p> <code>#context-name.slot-name</code> - The slot value "slot-name" in the context "context-name."</p> </li> <li> <p> <code>{attribute}</code> - The slot value of the session attribute "attribute."</p> </li> <li> <p> <code>'value'</code> - The discrete value "value."</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValue) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> SlotDefaultValue:
    out: SlotDefaultValue = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError("SlotDefaultValue.default_value required")
    return out
