"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetVisualList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.visual

TooltipSheetVisualList: TypeAlias = list["capo_quicksight.types.visual.Visual"]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetVisualList) -> list:
    import capo_quicksight.types.visual

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipSheetVisualList:
    import capo_quicksight.types.visual

    out: TooltipSheetVisualList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.visual.deserialize_json(item))
    return out


def redact_sensitive(value: TooltipSheetVisualList) -> list[Any]:
    import capo_quicksight.types.visual

    return [capo_quicksight.types.visual.redact_sensitive(item) for item in value]
