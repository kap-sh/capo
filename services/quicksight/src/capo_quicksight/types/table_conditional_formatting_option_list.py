"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.table_conditional_formatting_option

TableConditionalFormattingOptionList: TypeAlias = list[
    "capo_quicksight.types.table_conditional_formatting_option.TableConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormattingOptionList) -> list:
    import capo_quicksight.types.table_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.table_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TableConditionalFormattingOptionList:
    import capo_quicksight.types.table_conditional_formatting_option

    out: TableConditionalFormattingOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.table_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: TableConditionalFormattingOptionList) -> list[Any]:
    import capo_quicksight.types.table_conditional_formatting_option

    return [
        capo_quicksight.types.table_conditional_formatting_option.redact_sensitive(item)
        for item in value
    ]
