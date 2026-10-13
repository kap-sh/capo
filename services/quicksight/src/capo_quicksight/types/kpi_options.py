"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.comparison_configuration
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.kpi_sparkline_options
    import capo_quicksight.types.kpi_visual_layout_options
    import capo_quicksight.types.primary_value_display_type
    import capo_quicksight.types.progress_bar_options
    import capo_quicksight.types.secondary_value_options
    import capo_quicksight.types.trend_arrow_options


class KPIOptions(TypedDict, closed=True):
    progress_bar: NotRequired[
        "capo_quicksight.types.progress_bar_options.ProgressBarOptions"
    ]
    """<p>The options that determine the presentation of the progress bar of a KPI visual.</p>"""
    trend_arrows: NotRequired[
        "capo_quicksight.types.trend_arrow_options.TrendArrowOptions"
    ]
    """<p>The options that determine the presentation of trend arrows in a KPI visual.</p>"""
    secondary_value: NotRequired[
        "capo_quicksight.types.secondary_value_options.SecondaryValueOptions"
    ]
    """<p>The options that determine the presentation of the secondary value of a KPI visual.</p>"""
    comparison: NotRequired[
        "capo_quicksight.types.comparison_configuration.ComparisonConfiguration"
    ]
    """<p>The comparison configuration of a KPI visual.</p>"""
    primary_value_display_type: NotRequired[
        "capo_quicksight.types.primary_value_display_type.PrimaryValueDisplayType"
    ]
    """<p>The options that determine the primary value display type.</p>"""
    primary_value_font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The options that determine the primary value font configuration.</p>"""
    secondary_value_font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The options that determine the secondary value font configuration.</p>"""
    sparkline: NotRequired[
        "capo_quicksight.types.kpi_sparkline_options.KPISparklineOptions"
    ]
    """<p>The options that determine the visibility, color, type, and tooltip visibility of the sparkline of a KPI visual.</p>"""
    visual_layout_options: NotRequired[
        "capo_quicksight.types.kpi_visual_layout_options.KPIVisualLayoutOptions"
    ]
    """<p>The options that determine the layout a KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIOptions) -> dict:
    out: dict = {}
    if "progress_bar" in value:
        import capo_quicksight.types.progress_bar_options

        out["ProgressBar"] = capo_quicksight.types.progress_bar_options.serialize_json(
            value["progress_bar"]
        )
    if "trend_arrows" in value:
        import capo_quicksight.types.trend_arrow_options

        out["TrendArrows"] = capo_quicksight.types.trend_arrow_options.serialize_json(
            value["trend_arrows"]
        )
    if "secondary_value" in value:
        import capo_quicksight.types.secondary_value_options

        out["SecondaryValue"] = (
            capo_quicksight.types.secondary_value_options.serialize_json(
                value["secondary_value"]
            )
        )
    if "comparison" in value:
        import capo_quicksight.types.comparison_configuration

        out["Comparison"] = (
            capo_quicksight.types.comparison_configuration.serialize_json(
                value["comparison"]
            )
        )
    if "primary_value_display_type" in value:
        import capo_quicksight.types.primary_value_display_type

        out["PrimaryValueDisplayType"] = (
            capo_quicksight.types.primary_value_display_type.serialize_json(
                value["primary_value_display_type"]
            )
        )
    if "primary_value_font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["PrimaryValueFontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["primary_value_font_configuration"]
            )
        )
    if "secondary_value_font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["SecondaryValueFontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["secondary_value_font_configuration"]
            )
        )
    if "sparkline" in value:
        import capo_quicksight.types.kpi_sparkline_options

        out["Sparkline"] = capo_quicksight.types.kpi_sparkline_options.serialize_json(
            value["sparkline"]
        )
    if "visual_layout_options" in value:
        import capo_quicksight.types.kpi_visual_layout_options

        out["VisualLayoutOptions"] = (
            capo_quicksight.types.kpi_visual_layout_options.serialize_json(
                value["visual_layout_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIOptions:
    out: KPIOptions = {}  # type: ignore[typeddict-item]
    if data.get("ProgressBar") is not None:
        import capo_quicksight.types.progress_bar_options

        out["progress_bar"] = (
            capo_quicksight.types.progress_bar_options.deserialize_json(
                data["ProgressBar"]
            )
        )
    if data.get("TrendArrows") is not None:
        import capo_quicksight.types.trend_arrow_options

        out["trend_arrows"] = (
            capo_quicksight.types.trend_arrow_options.deserialize_json(
                data["TrendArrows"]
            )
        )
    if data.get("SecondaryValue") is not None:
        import capo_quicksight.types.secondary_value_options

        out["secondary_value"] = (
            capo_quicksight.types.secondary_value_options.deserialize_json(
                data["SecondaryValue"]
            )
        )
    if data.get("Comparison") is not None:
        import capo_quicksight.types.comparison_configuration

        out["comparison"] = (
            capo_quicksight.types.comparison_configuration.deserialize_json(
                data["Comparison"]
            )
        )
    if data.get("PrimaryValueDisplayType") is not None:
        import capo_quicksight.types.primary_value_display_type

        out["primary_value_display_type"] = (
            capo_quicksight.types.primary_value_display_type.deserialize_json(
                data["PrimaryValueDisplayType"]
            )
        )
    if data.get("PrimaryValueFontConfiguration") is not None:
        import capo_quicksight.types.font_configuration

        out["primary_value_font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["PrimaryValueFontConfiguration"]
            )
        )
    if data.get("SecondaryValueFontConfiguration") is not None:
        import capo_quicksight.types.font_configuration

        out["secondary_value_font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["SecondaryValueFontConfiguration"]
            )
        )
    if data.get("Sparkline") is not None:
        import capo_quicksight.types.kpi_sparkline_options

        out["sparkline"] = capo_quicksight.types.kpi_sparkline_options.deserialize_json(
            data["Sparkline"]
        )
    if data.get("VisualLayoutOptions") is not None:
        import capo_quicksight.types.kpi_visual_layout_options

        out["visual_layout_options"] = (
            capo_quicksight.types.kpi_visual_layout_options.deserialize_json(
                data["VisualLayoutOptions"]
            )
        )
    return out


def redact_sensitive(value: KPIOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comparison" in value:
        import capo_quicksight.types.comparison_configuration

        out["comparison"] = (
            capo_quicksight.types.comparison_configuration.redact_sensitive(
                value["comparison"]
            )
        )
    return out
