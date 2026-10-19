"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.slot_type_sort_attribute
    import capo_lex_models_v2.types.sort_order


class SlotTypeSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.slot_type_sort_attribute.SlotTypeSortAttribute"
    """<p>The attribute to use to sort the list of slot types.</p>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list. You can say ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.slot_type_sort_attribute

    out["attribute"] = capo_lex_models_v2.types.slot_type_sort_attribute.serialize_json(
        value["attribute"]
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> SlotTypeSortBy:
    out: SlotTypeSortBy = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_lex_models_v2.types.slot_type_sort_attribute

        out["attribute"] = (
            capo_lex_models_v2.types.slot_type_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_lex_models_v2.types.slot_type_sort_attribute.SlotTypeSortAttribute",
            "",
        )
    if data.get("order") is not None:
        import capo_lex_models_v2.types.sort_order

        out["order"] = capo_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        import typing

        out["order"] = typing.cast("capo_lex_models_v2.types.sort_order.SortOrder", "")
    return out
