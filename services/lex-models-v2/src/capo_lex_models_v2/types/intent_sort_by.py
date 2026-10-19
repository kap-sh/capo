"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_sort_attribute
    import capo_lex_models_v2.types.sort_order


class IntentSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.intent_sort_attribute.IntentSortAttribute"
    """<p>The attribute to use to sort the list of intents.</p>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list. You can choose ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.intent_sort_attribute

    out["attribute"] = capo_lex_models_v2.types.intent_sort_attribute.serialize_json(
        value["attribute"]
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> IntentSortBy:
    out: IntentSortBy = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_lex_models_v2.types.intent_sort_attribute

        out["attribute"] = (
            capo_lex_models_v2.types.intent_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_lex_models_v2.types.intent_sort_attribute.IntentSortAttribute", ""
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
