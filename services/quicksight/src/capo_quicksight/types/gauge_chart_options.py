"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arc_axis_configuration
    import capo_quicksight.types.arc_configuration
    import capo_quicksight.types.comparison_configuration
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.primary_value_display_type


class GaugeChartOptions(TypedDict, closed=True):
    primary_value_display_type: NotRequired[
        "capo_quicksight.types.primary_value_display_type.PrimaryValueDisplayType"
    ]
    """<p>The options that determine the primary value display type.</p>"""
    comparison: NotRequired[
        "capo_quicksight.types.comparison_configuration.ComparisonConfiguration"
    ]
    """<p>The comparison configuration of a <code>GaugeChartVisual</code>.</p>"""
    arc_axis: NotRequired[
        "capo_quicksight.types.arc_axis_configuration.ArcAxisConfiguration"
    ]
    """<p>The arc axis configuration of a <code>GaugeChartVisual</code>.</p>"""
    arc: NotRequired["capo_quicksight.types.arc_configuration.ArcConfiguration"]
    """<p>The arc configuration of a <code>GaugeChartVisual</code>.</p>"""
    primary_value_font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The options that determine the primary value font configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartOptions) -> dict:
    out: dict = {}
    if "primary_value_display_type" in value:
        import capo_quicksight.types.primary_value_display_type

        out["PrimaryValueDisplayType"] = (
            capo_quicksight.types.primary_value_display_type.serialize_json(
                value["primary_value_display_type"]
            )
        )
    if "comparison" in value:
        import capo_quicksight.types.comparison_configuration

        out["Comparison"] = (
            capo_quicksight.types.comparison_configuration.serialize_json(
                value["comparison"]
            )
        )
    if "arc_axis" in value:
        import capo_quicksight.types.arc_axis_configuration

        out["ArcAxis"] = capo_quicksight.types.arc_axis_configuration.serialize_json(
            value["arc_axis"]
        )
    if "arc" in value:
        import capo_quicksight.types.arc_configuration

        out["Arc"] = capo_quicksight.types.arc_configuration.serialize_json(
            value["arc"]
        )
    if "primary_value_font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["PrimaryValueFontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["primary_value_font_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartOptions:
    out: GaugeChartOptions = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValueDisplayType") is not None:
        import capo_quicksight.types.primary_value_display_type

        out["primary_value_display_type"] = (
            capo_quicksight.types.primary_value_display_type.deserialize_json(
                data["PrimaryValueDisplayType"]
            )
        )
    if data.get("Comparison") is not None:
        import capo_quicksight.types.comparison_configuration

        out["comparison"] = (
            capo_quicksight.types.comparison_configuration.deserialize_json(
                data["Comparison"]
            )
        )
    if data.get("ArcAxis") is not None:
        import capo_quicksight.types.arc_axis_configuration

        out["arc_axis"] = capo_quicksight.types.arc_axis_configuration.deserialize_json(
            data["ArcAxis"]
        )
    if data.get("Arc") is not None:
        import capo_quicksight.types.arc_configuration

        out["arc"] = capo_quicksight.types.arc_configuration.deserialize_json(
            data["Arc"]
        )
    if data.get("PrimaryValueFontConfiguration") is not None:
        import capo_quicksight.types.font_configuration

        out["primary_value_font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["PrimaryValueFontConfiguration"]
            )
        )
    return out


def redact_sensitive(value: GaugeChartOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comparison" in value:
        import capo_quicksight.types.comparison_configuration

        out["comparison"] = (
            capo_quicksight.types.comparison_configuration.redact_sensitive(
                value["comparison"]
            )
        )
    return out
