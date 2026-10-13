"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette
    import capo_quicksight.types.waterfall_chart_color_configuration
    import capo_quicksight.types.waterfall_chart_field_wells
    import capo_quicksight.types.waterfall_chart_options
    import capo_quicksight.types.waterfall_chart_sort_configuration


class WaterfallChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.waterfall_chart_field_wells.WaterfallChartFieldWells"
    ]
    """<p>The field well configuration of a waterfall visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.waterfall_chart_sort_configuration.WaterfallChartSortConfiguration"
    ]
    """<p>The sort configuration of a waterfall visual.</p>"""
    waterfall_chart_options: NotRequired[
        "capo_quicksight.types.waterfall_chart_options.WaterfallChartOptions"
    ]
    """<p>The options that determine the presentation of a waterfall visual.</p>"""
    category_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the category axis label.</p>"""
    category_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the category axis.</p>"""
    primary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the y-axis label.</p>"""
    primary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the y-axis.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend configuration of a waterfall visual.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a waterfall visual.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a waterfall visual.</p>"""
    color_configuration: NotRequired[
        "capo_quicksight.types.waterfall_chart_color_configuration.WaterfallChartColorConfiguration"
    ]
    """<p>The color configuration of a waterfall visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.waterfall_chart_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.waterfall_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.waterfall_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.waterfall_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "waterfall_chart_options" in value:
        import capo_quicksight.types.waterfall_chart_options

        out["WaterfallChartOptions"] = (
            capo_quicksight.types.waterfall_chart_options.serialize_json(
                value["waterfall_chart_options"]
            )
        )
    if "category_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["CategoryAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_axis_label_options"]
            )
        )
    if "category_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["CategoryAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["category_axis_display_options"]
            )
        )
    if "primary_y_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["PrimaryYAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["primary_y_axis_label_options"]
            )
        )
    if "primary_y_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["PrimaryYAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["primary_y_axis_display_options"]
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
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "color_configuration" in value:
        import capo_quicksight.types.waterfall_chart_color_configuration

        out["ColorConfiguration"] = (
            capo_quicksight.types.waterfall_chart_color_configuration.serialize_json(
                value["color_configuration"]
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


def deserialize_json(data: dict) -> WaterfallChartConfiguration:
    out: WaterfallChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.waterfall_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.waterfall_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.waterfall_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.waterfall_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("WaterfallChartOptions") is not None:
        import capo_quicksight.types.waterfall_chart_options

        out["waterfall_chart_options"] = (
            capo_quicksight.types.waterfall_chart_options.deserialize_json(
                data["WaterfallChartOptions"]
            )
        )
    if data.get("CategoryAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["category_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryAxisLabelOptions"]
            )
        )
    if data.get("CategoryAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["category_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["CategoryAxisDisplayOptions"]
            )
        )
    if data.get("PrimaryYAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["primary_y_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["PrimaryYAxisLabelOptions"]
            )
        )
    if data.get("PrimaryYAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["primary_y_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["PrimaryYAxisDisplayOptions"]
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
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("ColorConfiguration") is not None:
        import capo_quicksight.types.waterfall_chart_color_configuration

        out["color_configuration"] = (
            capo_quicksight.types.waterfall_chart_color_configuration.deserialize_json(
                data["ColorConfiguration"]
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


def redact_sensitive(value: WaterfallChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.waterfall_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.waterfall_chart_field_wells.redact_sensitive(
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
