"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.color_scale
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.tree_map_field_wells
    import capo_quicksight.types.tree_map_sort_configuration
    import capo_quicksight.types.visual_interaction_options


class TreeMapConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.tree_map_field_wells.TreeMapFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.tree_map_sort_configuration.TreeMapSortConfiguration"
    ]
    """<p>The sort configuration of a tree map.</p>"""
    group_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) of the groups that are displayed in a tree map.</p>"""
    size_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) of the sizes that are displayed in a tree map.</p>"""
    color_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility) for the colors displayed in a tree map.</p>"""
    color_scale: NotRequired["capo_quicksight.types.color_scale.ColorScale"]
    """<p>The color options (gradient color, point of divergence) of a tree map.</p>"""
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
def serialize_json(value: TreeMapConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.tree_map_field_wells

        out["FieldWells"] = capo_quicksight.types.tree_map_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.tree_map_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.tree_map_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "group_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["GroupLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["group_label_options"]
            )
        )
    if "size_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["SizeLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["size_label_options"]
            )
        )
    if "color_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
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


def deserialize_json(data: dict) -> TreeMapConfiguration:
    out: TreeMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.tree_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.tree_map_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.tree_map_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.tree_map_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("GroupLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["group_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["GroupLabelOptions"]
            )
        )
    if data.get("SizeLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["size_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["SizeLabelOptions"]
            )
        )
    if data.get("ColorLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
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


def redact_sensitive(value: TreeMapConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.tree_map_field_wells

        out["field_wells"] = (
            capo_quicksight.types.tree_map_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.redact_sensitive(
            value["data_labels"]
        )
    return out
