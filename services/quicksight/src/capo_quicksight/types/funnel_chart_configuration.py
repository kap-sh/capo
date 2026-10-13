"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.funnel_chart_data_label_options
    import capo_quicksight.types.funnel_chart_field_wells
    import capo_quicksight.types.funnel_chart_sort_configuration
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class FunnelChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.funnel_chart_field_wells.FunnelChartFieldWells"
    ]
    """<p>The field well configuration of a <code>FunnelChartVisual</code>.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.funnel_chart_sort_configuration.FunnelChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>FunnelChartVisual</code>.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the categories that are displayed in a <code>FunnelChartVisual</code>.</p>"""
    value_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options for the values that are displayed in a <code>FunnelChartVisual</code>.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a <code>FunnelChartVisual</code>.</p>"""
    data_label_options: NotRequired[
        "capo_quicksight.types.funnel_chart_data_label_options.FunnelChartDataLabelOptions"
    ]
    """<p>The options that determine the presentation of the data labels.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a <code>FunnelChartVisual</code>.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.funnel_chart_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.funnel_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.funnel_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.funnel_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "category_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "value_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ValueLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["value_label_options"]
            )
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "data_label_options" in value:
        import capo_quicksight.types.funnel_chart_data_label_options

        out["DataLabelOptions"] = (
            capo_quicksight.types.funnel_chart_data_label_options.serialize_json(
                value["data_label_options"]
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


def deserialize_json(data: dict) -> FunnelChartConfiguration:
    out: FunnelChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.funnel_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.funnel_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.funnel_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.funnel_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("CategoryLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if data.get("ValueLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["value_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ValueLabelOptions"]
            )
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("DataLabelOptions") is not None:
        import capo_quicksight.types.funnel_chart_data_label_options

        out["data_label_options"] = (
            capo_quicksight.types.funnel_chart_data_label_options.deserialize_json(
                data["DataLabelOptions"]
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


def redact_sensitive(value: FunnelChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.funnel_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.funnel_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
