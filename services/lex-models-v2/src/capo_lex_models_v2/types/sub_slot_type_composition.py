"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SubSlotTypeComposition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.built_in_or_custom_slot_type_id
    import capo_lex_models_v2.types.name


class SubSlotTypeComposition(TypedDict, closed=True):
    name: "capo_lex_models_v2.types.name.Name"
    """<p>Name of a constituent sub slot inside a composite slot.</p>"""
    slot_type_id: "capo_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    """<p>The unique identifier assigned to a slot type. This refers to either a built-in slot type or the unique slotTypeId of a custom slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubSlotTypeComposition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["slotTypeId"] = value["slot_type_id"]
    return out


def deserialize_json(data: dict) -> SubSlotTypeComposition:
    out: SubSlotTypeComposition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("slotTypeId") is not None:
        out["slot_type_id"] = data["slotTypeId"]
    else:
        out["slot_type_id"] = ""
    return out
