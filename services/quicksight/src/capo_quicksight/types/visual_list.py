"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.visual

VisualList: TypeAlias = list["capo_quicksight.types.visual.Visual"]


# --- restJson1 ser/de ---
def serialize_json(value: VisualList) -> list:
    import capo_quicksight.types.visual

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> VisualList:
    import capo_quicksight.types.visual

    out: VisualList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.visual.deserialize_json(item))
    return out


def redact_sensitive(value: VisualList) -> list[Any]:
    import capo_quicksight.types.visual

    return [capo_quicksight.types.visual.redact_sensitive(item) for item in value]
