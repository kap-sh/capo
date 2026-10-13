"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConditionalFormattingOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.gauge_chart_arc_conditional_formatting
    import capo_quicksight.types.gauge_chart_primary_value_conditional_formatting


class GaugeChartConditionalFormattingOption(TypedDict, closed=True):
    primary_value: NotRequired[
        "capo_quicksight.types.gauge_chart_primary_value_conditional_formatting.GaugeChartPrimaryValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the primary value of a <code>GaugeChartVisual</code>.</p>"""
    arc: NotRequired[
        "capo_quicksight.types.gauge_chart_arc_conditional_formatting.GaugeChartArcConditionalFormatting"
    ]
    """<p>The options that determine the presentation of the arc of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConditionalFormattingOption) -> dict:
    out: dict = {}
    if "primary_value" in value:
        import capo_quicksight.types.gauge_chart_primary_value_conditional_formatting

        out["PrimaryValue"] = (
            capo_quicksight.types.gauge_chart_primary_value_conditional_formatting.serialize_json(
                value["primary_value"]
            )
        )
    if "arc" in value:
        import capo_quicksight.types.gauge_chart_arc_conditional_formatting

        out["Arc"] = (
            capo_quicksight.types.gauge_chart_arc_conditional_formatting.serialize_json(
                value["arc"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartConditionalFormattingOption:
    out: GaugeChartConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValue") is not None:
        import capo_quicksight.types.gauge_chart_primary_value_conditional_formatting

        out["primary_value"] = (
            capo_quicksight.types.gauge_chart_primary_value_conditional_formatting.deserialize_json(
                data["PrimaryValue"]
            )
        )
    if data.get("Arc") is not None:
        import capo_quicksight.types.gauge_chart_arc_conditional_formatting

        out["arc"] = (
            capo_quicksight.types.gauge_chart_arc_conditional_formatting.deserialize_json(
                data["Arc"]
            )
        )
    return out


def redact_sensitive(value: GaugeChartConditionalFormattingOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_value" in value:
        import capo_quicksight.types.gauge_chart_primary_value_conditional_formatting

        out["primary_value"] = (
            capo_quicksight.types.gauge_chart_primary_value_conditional_formatting.redact_sensitive(
                value["primary_value"]
            )
        )
    if "arc" in value:
        import capo_quicksight.types.gauge_chart_arc_conditional_formatting

        out["arc"] = (
            capo_quicksight.types.gauge_chart_arc_conditional_formatting.redact_sensitive(
                value["arc"]
            )
        )
    return out
