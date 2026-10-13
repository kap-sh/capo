"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.layout

LayoutList: TypeAlias = list["capo_quicksight.types.layout.Layout"]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutList) -> list:
    import capo_quicksight.types.layout

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.layout.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayoutList:
    import capo_quicksight.types.layout

    out: LayoutList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.layout.deserialize_json(item))
    return out


def redact_sensitive(value: LayoutList) -> list[Any]:
    import capo_quicksight.types.layout

    return [capo_quicksight.types.layout.redact_sensitive(item) for item in value]
