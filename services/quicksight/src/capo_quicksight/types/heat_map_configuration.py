"""Generated from Smithy shape ``com.amazonaws.quicksight#HeatMapConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.color_scale
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.heat_map_field_wells
    import capo_quicksight.types.heat_map_sort_configuration
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options


class HeatMapConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.heat_map_field_wells.HeatMapFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.heat_map_sort_configuration.HeatMapSortConfiguration"
    ]
    """<p>The sort configuration of a heat map.</p>"""
    row_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the row axis label.</p>"""
    row_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the row that is displayed in a <code>heat map</code>.</p>"""
    column_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the row axis label.</p>"""
    column_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the column that is displayed in a heat map.</p>"""
    color_scale: NotRequired["capo_quicksight.types.color_scale.ColorScale"]
    """<p>The color options (gradient color, point of divergence) in a heat map.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeatMapConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.heat_map_field_wells

        out["FieldWells"] = capo_quicksight.types.heat_map_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.heat_map_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.heat_map_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "row_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["RowAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["row_axis_display_options"]
            )
        )
    if "row_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["RowLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["row_label_options"]
            )
        )
    if "column_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["ColumnAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["column_axis_display_options"]
            )
        )
    if "column_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ColumnLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["column_label_options"]
            )
        )
    if "color_scale" in value:
        import capo_quicksight.types.color_scale

        out["ColorScale"] = capo_quicksight.types.color_scale.serialize_json(
            value["color_scale"]
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
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> HeatMapConfiguration:
    out: HeatMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.heat_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.heat_map_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.heat_map_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.heat_map_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("RowAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["row_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["RowAxisDisplayOptions"]
            )
        )
    if data.get("RowLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["row_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["RowLabelOptions"]
            )
        )
    if data.get("ColumnAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["column_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["ColumnAxisDisplayOptions"]
            )
        )
    if data.get("ColumnLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["column_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColumnLabelOptions"]
            )
        )
    if data.get("ColorScale") is not None:
        import capo_quicksight.types.color_scale

        out["color_scale"] = capo_quicksight.types.color_scale.deserialize_json(
            data["ColorScale"]
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
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: HeatMapConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.heat_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.heat_map_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.redact_sensitive(
            value["data_labels"]
        )
    return out
