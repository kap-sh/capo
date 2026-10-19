"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#SlotDefaultValueSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.slot_default_value_list


class SlotDefaultValueSpec(TypedDict, closed=True):
    default_value_list: "capo_lex_model_building_service.types.slot_default_value_list.SlotDefaultValueList"
    """<p>The default values for a slot. You can specify more than one default. For example, you can specify a default value to use from a matching context variable, a session attribute, or a fixed value.</p> <p>The default value chosen is selected based on the order that you specify them in the list. For example, if you specify a context variable and a fixed value in that order, Amazon Lex uses the context variable if it is available, else it uses the fixed value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValueSpec) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.slot_default_value_list

    out["defaultValueList"] = (
        capo_lex_model_building_service.types.slot_default_value_list.serialize_json(
            value["default_value_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotDefaultValueSpec:
    out: SlotDefaultValueSpec = {}  # type: ignore[typeddict-item]
    if data.get("defaultValueList") is not None:
        import capo_lex_model_building_service.types.slot_default_value_list

        out["default_value_list"] = (
            capo_lex_model_building_service.types.slot_default_value_list.deserialize_json(
                data["defaultValueList"]
            )
        )
    else:
        out["default_value_list"] = []
    return out
