"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.box_plot_field_wells
    import capo_quicksight.types.box_plot_options
    import capo_quicksight.types.box_plot_sort_configuration
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.reference_line_list
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class BoxPlotChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.box_plot_field_wells.BoxPlotFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.box_plot_sort_configuration.BoxPlotSortConfiguration"
    ]
    """<p>The sort configuration of a <code>BoxPlotVisual</code>.</p>"""
    box_plot_options: NotRequired[
        "capo_quicksight.types.box_plot_options.BoxPlotOptions"
    ]
    """<p>The box plot chart options for a box plot visual</p>"""
    category_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) of a box plot category.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort Icon visibility) of a box plot category.</p>"""
    primary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) of a box plot category.</p>"""
    primary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) of a box plot value.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
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
def serialize_json(value: BoxPlotChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.box_plot_field_wells

        out["FieldWells"] = capo_quicksight.types.box_plot_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.box_plot_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.box_plot_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "box_plot_options" in value:
        import capo_quicksight.types.box_plot_options

        out["BoxPlotOptions"] = capo_quicksight.types.box_plot_options.serialize_json(
            value["box_plot_options"]
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
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
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


def deserialize_json(data: dict) -> BoxPlotChartConfiguration:
    out: BoxPlotChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.box_plot_field_wells

        out["field_wells"] = (
            capo_quicksight.types.box_plot_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.box_plot_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.box_plot_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("BoxPlotOptions") is not None:
        import capo_quicksight.types.box_plot_options

        out["box_plot_options"] = (
            capo_quicksight.types.box_plot_options.deserialize_json(
                data["BoxPlotOptions"]
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
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
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


def redact_sensitive(value: BoxPlotChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.box_plot_field_wells

        out["field_wells"] = (
            capo_quicksight.types.box_plot_field_wells.redact_sensitive(
                value["field_wells"]
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
