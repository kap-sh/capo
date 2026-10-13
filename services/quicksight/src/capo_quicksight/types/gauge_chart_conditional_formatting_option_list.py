"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.gauge_chart_conditional_formatting_option

GaugeChartConditionalFormattingOptionList: TypeAlias = list[
    "capo_quicksight.types.gauge_chart_conditional_formatting_option.GaugeChartConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConditionalFormattingOptionList) -> list:
    import capo_quicksight.types.gauge_chart_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.gauge_chart_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GaugeChartConditionalFormattingOptionList:
    import capo_quicksight.types.gauge_chart_conditional_formatting_option

    out: GaugeChartConditionalFormattingOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.gauge_chart_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GaugeChartConditionalFormattingOptionList) -> list[Any]:
    import capo_quicksight.types.gauge_chart_conditional_formatting_option

    return [
        capo_quicksight.types.gauge_chart_conditional_formatting_option.redact_sensitive(
            item
        )
        for item in value
    ]
