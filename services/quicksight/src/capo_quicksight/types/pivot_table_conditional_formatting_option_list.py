"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_conditional_formatting_option

PivotTableConditionalFormattingOptionList: TypeAlias = list[
    "capo_quicksight.types.pivot_table_conditional_formatting_option.PivotTableConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingOptionList) -> list:
    import capo_quicksight.types.pivot_table_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.pivot_table_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PivotTableConditionalFormattingOptionList:
    import capo_quicksight.types.pivot_table_conditional_formatting_option

    out: PivotTableConditionalFormattingOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.pivot_table_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: PivotTableConditionalFormattingOptionList) -> list[Any]:
    import capo_quicksight.types.pivot_table_conditional_formatting_option

    return [
        capo_quicksight.types.pivot_table_conditional_formatting_option.redact_sensitive(
            item
        )
        for item in value
    ]
