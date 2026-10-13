"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.kpi_conditional_formatting_option

KPIConditionalFormattingOptionList: TypeAlias = list[
    "capo_quicksight.types.kpi_conditional_formatting_option.KPIConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: KPIConditionalFormattingOptionList) -> list:
    import capo_quicksight.types.kpi_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.kpi_conditional_formatting_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KPIConditionalFormattingOptionList:
    import capo_quicksight.types.kpi_conditional_formatting_option

    out: KPIConditionalFormattingOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.kpi_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: KPIConditionalFormattingOptionList) -> list[Any]:
    import capo_quicksight.types.kpi_conditional_formatting_option

    return [
        capo_quicksight.types.kpi_conditional_formatting_option.redact_sensitive(item)
        for item in value
    ]
