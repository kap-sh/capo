"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Specifications``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.built_in_or_custom_slot_type_id
    import capo_lex_models_v2.types.sub_slot_value_elicitation_setting


class Specifications(TypedDict, closed=True):
    slot_type_id: "capo_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
    """<p>The unique identifier assigned to the slot type.</p>"""
    value_elicitation_setting: "capo_lex_models_v2.types.sub_slot_value_elicitation_setting.SubSlotValueElicitationSetting"
    """<p>Specifies the elicitation setting details for constituent sub slots of a composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Specifications) -> dict:
    out: dict = {}
    out["slotTypeId"] = value["slot_type_id"]
    import capo_lex_models_v2.types.sub_slot_value_elicitation_setting

    out["valueElicitationSetting"] = (
        capo_lex_models_v2.types.sub_slot_value_elicitation_setting.serialize_json(
            value["value_elicitation_setting"]
        )
    )
    return out


def deserialize_json(data: dict) -> Specifications:
    out: Specifications = {}  # type: ignore[typeddict-item]
    if data.get("slotTypeId") is not None:
        out["slot_type_id"] = data["slotTypeId"]
    else:
        out["slot_type_id"] = ""
    if data.get("valueElicitationSetting") is not None:
        import capo_lex_models_v2.types.sub_slot_value_elicitation_setting

        out["value_elicitation_setting"] = (
            capo_lex_models_v2.types.sub_slot_value_elicitation_setting.deserialize_json(
                data["valueElicitationSetting"]
            )
        )
    else:
        raise DeserializationError("Specifications.value_elicitation_setting required")
    return out
