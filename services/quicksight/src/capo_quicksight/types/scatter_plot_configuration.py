"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.scatter_plot_field_wells
    import capo_quicksight.types.scatter_plot_sort_configuration
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class ScatterPlotConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.scatter_plot_field_wells.ScatterPlotFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.scatter_plot_sort_configuration.ScatterPlotSortConfiguration"
    ]
    """<p>The sort configuration of a scatter plot.</p>"""
    x_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of the scatter plot's x-axis.</p>"""
    x_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, and axis step) of the scatter plot's x-axis.</p>"""
    y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of the scatter plot's y-axis.</p>"""
    y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, and axis step) of the scatter plot's y-axis.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The legend display setup of the visual.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.scatter_plot_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.scatter_plot_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.scatter_plot_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.scatter_plot_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "x_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["XAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["x_axis_label_options"]
            )
        )
    if "x_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["XAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["x_axis_display_options"]
            )
        )
    if "y_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["YAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["y_axis_label_options"]
            )
        )
    if "y_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["YAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["y_axis_display_options"]
            )
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


def deserialize_json(data: dict) -> ScatterPlotConfiguration:
    out: ScatterPlotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.scatter_plot_field_wells

        out["field_wells"] = (
            capo_quicksight.types.scatter_plot_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.scatter_plot_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.scatter_plot_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("XAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["x_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["XAxisLabelOptions"]
            )
        )
    if data.get("XAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["x_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["XAxisDisplayOptions"]
            )
        )
    if data.get("YAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["y_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["YAxisLabelOptions"]
            )
        )
    if data.get("YAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["y_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["YAxisDisplayOptions"]
            )
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


def redact_sensitive(value: ScatterPlotConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.scatter_plot_field_wells

        out["field_wells"] = (
            capo_quicksight.types.scatter_plot_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.redact_sensitive(
            value["data_labels"]
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
