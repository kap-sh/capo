"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFromLayoutElementList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.free_form_layout_element

FreeFromLayoutElementList: TypeAlias = list[
    "capo_quicksight.types.free_form_layout_element.FreeFormLayoutElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeFromLayoutElementList) -> list:
    import capo_quicksight.types.free_form_layout_element

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.free_form_layout_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeFromLayoutElementList:
    import capo_quicksight.types.free_form_layout_element

    out: FreeFromLayoutElementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.free_form_layout_element.deserialize_json(item)
        )
    return out


def redact_sensitive(value: FreeFromLayoutElementList) -> list[Any]:
    import capo_quicksight.types.free_form_layout_element

    return [
        capo_quicksight.types.free_form_layout_element.redact_sensitive(item)
        for item in value
    ]
