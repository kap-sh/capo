"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetDefinitionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.tooltip_sheet_definition

TooltipSheetDefinitionList: TypeAlias = list[
    "capo_quicksight.types.tooltip_sheet_definition.TooltipSheetDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetDefinitionList) -> list:
    import capo_quicksight.types.tooltip_sheet_definition

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.tooltip_sheet_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipSheetDefinitionList:
    import capo_quicksight.types.tooltip_sheet_definition

    out: TooltipSheetDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.tooltip_sheet_definition.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TooltipSheetDefinitionList) -> list[Any]:
    import capo_quicksight.types.tooltip_sheet_definition

    return [
        capo_quicksight.types.tooltip_sheet_definition.redact_sensitive(item)
        for item in value
    ]
