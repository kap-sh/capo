"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.bar_chart_default_series_settings
    import capo_quicksight.types.bar_chart_field_wells
    import capo_quicksight.types.bar_chart_orientation
    import capo_quicksight.types.bar_chart_sort_configuration
    import capo_quicksight.types.bar_series_item_list
    import capo_quicksight.types.bars_arrangement
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.contribution_analysis_default_list
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.reference_line_list
    import capo_quicksight.types.small_multiples_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class BarChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.bar_chart_field_wells.BarChartFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.bar_chart_sort_configuration.BarChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>BarChartVisual</code>.</p>"""
    orientation: NotRequired[
        "capo_quicksight.types.bar_chart_orientation.BarChartOrientation"
    ]
    """<p>The orientation of the bars in a bar chart visual. There are two valid values in this structure:</p> <ul> <li> <p> <code>HORIZONTAL</code>: Used for charts that have horizontal bars. Visuals that use this value are horizontal bar charts, horizontal stacked bar charts, and horizontal stacked 100% bar charts.</p> </li> <li> <p> <code>VERTICAL</code>: Used for charts that have vertical bars. Visuals that use this value are vertical bar charts, vertical stacked bar charts, and vertical stacked 100% bar charts.</p> </li> </ul>"""
    bars_arrangement: NotRequired[
        "capo_quicksight.types.bars_arrangement.BarsArrangement"
    ]
    """<p>Determines the arrangement of the bars. The orientation and arrangement of bars determine the type of bar that is used in the visual.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    small_multiples_options: NotRequired[
        "capo_quicksight.types.small_multiples_options.SmallMultiplesOptions"
    ]
    """<p>The small multiples setup for the visual.</p>"""
    category_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) for bar chart category.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a bar chart.</p>"""
    value_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) for a bar chart value.</p>"""
    value_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a bar chart value.</p>"""
    color_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a color that is used in a bar chart.</p>"""
    default_series_settings: NotRequired[
        "capo_quicksight.types.bar_chart_default_series_settings.BarChartDefaultSeriesSettings"
    ]
    """<p>The options that determine the default presentation of all bar series in <code>BarChartVisual</code>.</p>"""
    series: NotRequired["capo_quicksight.types.bar_series_item_list.BarSeriesItemList"]
    """<p>The series item configuration of a <code>BarChartVisual</code>.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    reference_lines: NotRequired[
        "capo_quicksight.types.reference_line_list.ReferenceLineList"
    ]
    """<p>The reference line setup of the visual.</p>"""
    contribution_analysis_defaults: NotRequired[
        "capo_quicksight.types.contribution_analysis_default_list.ContributionAnalysisDefaultList"
    ]
    """<p>The contribution analysis (anomaly configuration) setup of the visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.bar_chart_field_wells

        out["FieldWells"] = capo_quicksight.types.bar_chart_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.bar_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.bar_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "orientation" in value:
        import capo_quicksight.types.bar_chart_orientation

        out["Orientation"] = capo_quicksight.types.bar_chart_orientation.serialize_json(
            value["orientation"]
        )
    if "bars_arrangement" in value:
        import capo_quicksight.types.bars_arrangement

        out["BarsArrangement"] = capo_quicksight.types.bars_arrangement.serialize_json(
            value["bars_arrangement"]
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "small_multiples_options" in value:
        import capo_quicksight.types.small_multiples_options

        out["SmallMultiplesOptions"] = (
            capo_quicksight.types.small_multiples_options.serialize_json(
                value["small_multiples_options"]
            )
        )
    if "category_axis" in value:
        import capo_quicksight.types.axis_display_options

        out["CategoryAxis"] = capo_quicksight.types.axis_display_options.serialize_json(
            value["category_axis"]
        )
    if "category_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "value_axis" in value:
        import capo_quicksight.types.axis_display_options

        out["ValueAxis"] = capo_quicksight.types.axis_display_options.serialize_json(
            value["value_axis"]
        )
    if "value_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ValueLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["value_label_options"]
            )
        )
    if "color_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
            )
        )
    if "default_series_settings" in value:
        import capo_quicksight.types.bar_chart_default_series_settings

        out["DefaultSeriesSettings"] = (
            capo_quicksight.types.bar_chart_default_series_settings.serialize_json(
                value["default_series_settings"]
            )
        )
    if "series" in value:
        import capo_quicksight.types.bar_series_item_list

        out["Series"] = capo_quicksight.types.bar_series_item_list.serialize_json(
            value["series"]
        )
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["DataLabels"] = capo_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "reference_lines" in value:
        import capo_quicksight.types.reference_line_list

        out["ReferenceLines"] = (
            capo_quicksight.types.reference_line_list.serialize_json(
                value["reference_lines"]
            )
        )
    if "contribution_analysis_defaults" in value:
        import capo_quicksight.types.contribution_analysis_default_list

        out["ContributionAnalysisDefaults"] = (
            capo_quicksight.types.contribution_analysis_default_list.serialize_json(
                value["contribution_analysis_defaults"]
            )
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartConfiguration:
    out: BarChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.bar_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.bar_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.bar_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.bar_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("Orientation") is not None:
        import capo_quicksight.types.bar_chart_orientation

        out["orientation"] = (
            capo_quicksight.types.bar_chart_orientation.deserialize_json(
                data["Orientation"]
            )
        )
    if data.get("BarsArrangement") is not None:
        import capo_quicksight.types.bars_arrangement

        out["bars_arrangement"] = (
            capo_quicksight.types.bars_arrangement.deserialize_json(
                data["BarsArrangement"]
            )
        )
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("SmallMultiplesOptions") is not None:
        import capo_quicksight.types.small_multiples_options

        out["small_multiples_options"] = (
            capo_quicksight.types.small_multiples_options.deserialize_json(
                data["SmallMultiplesOptions"]
            )
        )
    if data.get("CategoryAxis") is not None:
        import capo_quicksight.types.axis_display_options

        out["category_axis"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["CategoryAxis"]
            )
        )
    if data.get("CategoryLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if data.get("ValueAxis") is not None:
        import capo_quicksight.types.axis_display_options

        out["value_axis"] = capo_quicksight.types.axis_display_options.deserialize_json(
            data["ValueAxis"]
        )
    if data.get("ValueLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["value_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ValueLabelOptions"]
            )
        )
    if data.get("ColorLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
            )
        )
    if data.get("DefaultSeriesSettings") is not None:
        import capo_quicksight.types.bar_chart_default_series_settings

        out["default_series_settings"] = (
            capo_quicksight.types.bar_chart_default_series_settings.deserialize_json(
                data["DefaultSeriesSettings"]
            )
        )
    if data.get("Series") is not None:
        import capo_quicksight.types.bar_series_item_list

        out["series"] = capo_quicksight.types.bar_series_item_list.deserialize_json(
            data["Series"]
        )
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if data.get("DataLabels") is not None:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.deserialize_json(
            data["DataLabels"]
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("ReferenceLines") is not None:
        import capo_quicksight.types.reference_line_list

        out["reference_lines"] = (
            capo_quicksight.types.reference_line_list.deserialize_json(
                data["ReferenceLines"]
            )
        )
    if data.get("ContributionAnalysisDefaults") is not None:
        import capo_quicksight.types.contribution_analysis_default_list

        out["contribution_analysis_defaults"] = (
            capo_quicksight.types.contribution_analysis_default_list.deserialize_json(
                data["ContributionAnalysisDefaults"]
            )
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: BarChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.bar_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.bar_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    if "series" in value:
        import capo_quicksight.types.bar_series_item_list

        out["series"] = capo_quicksight.types.bar_series_item_list.redact_sensitive(
            value["series"]
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.redact_sensitive(
            value["data_labels"]
        )
    if "reference_lines" in value:
        import capo_quicksight.types.reference_line_list

        out["reference_lines"] = (
            capo_quicksight.types.reference_line_list.redact_sensitive(
                value["reference_lines"]
            )
        )
    return out
