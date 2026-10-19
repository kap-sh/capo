"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.generation_sort_by_attribute
    import capo_lex_models_v2.types.sort_order


class GenerationSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.generation_sort_by_attribute.GenerationSortByAttribute"
    """<p>The attribute by which to sort the generation request information. You can sort by the following attributes.</p> <ul> <li> <p> <code>creationStartTime</code> – The time at which the generation request was created.</p> </li> <li> <p> <code>lastUpdatedTime</code> – The time at which the generation request was last updated.</p> </li> </ul>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order by which to sort the generation request information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.generation_sort_by_attribute

    out["attribute"] = (
        capo_lex_models_v2.types.generation_sort_by_attribute.serialize_json(
            value["attribute"]
        )
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> GenerationSortBy:
    out: GenerationSortBy = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_lex_models_v2.types.generation_sort_by_attribute

        out["attribute"] = (
            capo_lex_models_v2.types.generation_sort_by_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        import typing

        out["attribute"] = typing.cast(
            "capo_lex_models_v2.types.generation_sort_by_attribute.GenerationSortByAttribute",
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
