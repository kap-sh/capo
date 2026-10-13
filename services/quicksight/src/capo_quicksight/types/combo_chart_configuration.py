"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.bars_arrangement
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.combo_chart_default_series_settings
    import capo_quicksight.types.combo_chart_field_wells
    import capo_quicksight.types.combo_chart_sort_configuration
    import capo_quicksight.types.combo_series_item_list
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.reference_line_list
    import capo_quicksight.types.single_axis_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class ComboChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.combo_chart_field_wells.ComboChartFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.combo_chart_sort_configuration.ComboChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>ComboChartVisual</code>.</p>"""
    bars_arrangement: NotRequired[
        "capo_quicksight.types.bars_arrangement.BarsArrangement"
    ]
    """<p>Determines the bar arrangement in a combo chart. The following are valid values in this structure:</p> <ul> <li> <p> <code>CLUSTERED</code>: For clustered bar combo charts.</p> </li> <li> <p> <code>STACKED</code>: For stacked bar combo charts.</p> </li> <li> <p> <code>STACKED_PERCENT</code>: Do not use. If you use this value, the operation returns a validation error.</p> </li> </ul>"""
    category_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The category axis of a combo chart.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of a combo chart category (group/color) field well.</p>"""
    primary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, and axis step) of a combo chart's primary y-axis (bar) field well.</p>"""
    primary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of a combo chart's primary y-axis (bar) field well.</p>"""
    secondary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) of a combo chart's secondary y-axis (line) field well.</p>"""
    secondary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of a combo chart's secondary y-axis(line) field well.</p>"""
    single_axis_options: NotRequired[
        "capo_quicksight.types.single_axis_options.SingleAxisOptions"
    ]
    color_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of a combo chart's color field well.</p>"""
    default_series_settings: NotRequired[
        "capo_quicksight.types.combo_chart_default_series_settings.ComboChartDefaultSeriesSettings"
    ]
    """<p>The options that determine the default presentation of all series in <code>ComboChartVisual</code>.</p>"""
    series: NotRequired[
        "capo_quicksight.types.combo_series_item_list.ComboSeriesItemList"
    ]
    """<p>The series item configuration of a <code>ComboChartVisual</code>.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    bar_data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p> <p>The data label options for a bar in a combo chart.</p>"""
    line_data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p> <p>The data label options for a line in a combo chart.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The legend display setup of the visual.</p>"""
    reference_lines: NotRequired[
        "capo_quicksight.types.reference_line_list.ReferenceLineList"
    ]
    """<p>The reference line setup of the visual.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.combo_chart_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.combo_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.combo_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.combo_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "bars_arrangement" in value:
        import capo_quicksight.types.bars_arrangement

        out["BarsArrangement"] = capo_quicksight.types.bars_arrangement.serialize_json(
            value["bars_arrangement"]
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
    if "primary_y_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["PrimaryYAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["primary_y_axis_display_options"]
            )
        )
    if "primary_y_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["PrimaryYAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["primary_y_axis_label_options"]
            )
        )
    if "secondary_y_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["SecondaryYAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["secondary_y_axis_display_options"]
            )
        )
    if "secondary_y_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["SecondaryYAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["secondary_y_axis_label_options"]
            )
        )
    if "single_axis_options" in value:
        import capo_quicksight.types.single_axis_options

        out["SingleAxisOptions"] = (
            capo_quicksight.types.single_axis_options.serialize_json(
                value["single_axis_options"]
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
        import capo_quicksight.types.combo_chart_default_series_settings

        out["DefaultSeriesSettings"] = (
            capo_quicksight.types.combo_chart_default_series_settings.serialize_json(
                value["default_series_settings"]
            )
        )
    if "series" in value:
        import capo_quicksight.types.combo_series_item_list

        out["Series"] = capo_quicksight.types.combo_series_item_list.serialize_json(
            value["series"]
        )
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "bar_data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["BarDataLabels"] = capo_quicksight.types.data_label_options.serialize_json(
            value["bar_data_labels"]
        )
    if "line_data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["LineDataLabels"] = capo_quicksight.types.data_label_options.serialize_json(
            value["line_data_labels"]
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
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboChartConfiguration:
    out: ComboChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.combo_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.combo_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.combo_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.combo_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("BarsArrangement") is not None:
        import capo_quicksight.types.bars_arrangement

        out["bars_arrangement"] = (
            capo_quicksight.types.bars_arrangement.deserialize_json(
                data["BarsArrangement"]
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
    if data.get("PrimaryYAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["primary_y_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["PrimaryYAxisDisplayOptions"]
            )
        )
    if data.get("PrimaryYAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["primary_y_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["PrimaryYAxisLabelOptions"]
            )
        )
    if data.get("SecondaryYAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["secondary_y_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["SecondaryYAxisDisplayOptions"]
            )
        )
    if data.get("SecondaryYAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["secondary_y_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["SecondaryYAxisLabelOptions"]
            )
        )
    if data.get("SingleAxisOptions") is not None:
        import capo_quicksight.types.single_axis_options

        out["single_axis_options"] = (
            capo_quicksight.types.single_axis_options.deserialize_json(
                data["SingleAxisOptions"]
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
        import capo_quicksight.types.combo_chart_default_series_settings

        out["default_series_settings"] = (
            capo_quicksight.types.combo_chart_default_series_settings.deserialize_json(
                data["DefaultSeriesSettings"]
            )
        )
    if data.get("Series") is not None:
        import capo_quicksight.types.combo_series_item_list

        out["series"] = capo_quicksight.types.combo_series_item_list.deserialize_json(
            data["Series"]
        )
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if data.get("BarDataLabels") is not None:
        import capo_quicksight.types.data_label_options

        out["bar_data_labels"] = (
            capo_quicksight.types.data_label_options.deserialize_json(
                data["BarDataLabels"]
            )
        )
    if data.get("LineDataLabels") is not None:
        import capo_quicksight.types.data_label_options

        out["line_data_labels"] = (
            capo_quicksight.types.data_label_options.deserialize_json(
                data["LineDataLabels"]
            )
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
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: ComboChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.combo_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.combo_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "series" in value:
        import capo_quicksight.types.combo_series_item_list

        out["series"] = capo_quicksight.types.combo_series_item_list.redact_sensitive(
            value["series"]
        )
    if "bar_data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["bar_data_labels"] = (
            capo_quicksight.types.data_label_options.redact_sensitive(
                value["bar_data_labels"]
            )
        )
    if "line_data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["line_data_labels"] = (
            capo_quicksight.types.data_label_options.redact_sensitive(
                value["line_data_labels"]
            )
        )
    if "reference_lines" in value:
        import capo_quicksight.types.reference_line_list

        out["reference_lines"] = (
            capo_quicksight.types.reference_line_list.redact_sensitive(
                value["reference_lines"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
