"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotDefaultValueSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_default_value_list


class SlotDefaultValueSpecification(TypedDict, closed=True):
    default_value_list: (
        "capo_lex_models_v2.types.slot_default_value_list.SlotDefaultValueList"
    )
    """<p>A list of default values. Amazon Lex chooses the default value to use in the order that they are presented in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotDefaultValueSpecification) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.slot_default_value_list

    out["defaultValueList"] = (
        capo_lex_models_v2.types.slot_default_value_list.serialize_json(
            value["default_value_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> SlotDefaultValueSpecification:
    out: SlotDefaultValueSpecification = {}  # type: ignore[typeddict-item]
    if data.get("defaultValueList") is not None:
        import capo_lex_models_v2.types.slot_default_value_list

        out["default_value_list"] = (
            capo_lex_models_v2.types.slot_default_value_list.deserialize_json(
                data["defaultValueList"]
            )
        )
    else:
        out["default_value_list"] = []
    return out
