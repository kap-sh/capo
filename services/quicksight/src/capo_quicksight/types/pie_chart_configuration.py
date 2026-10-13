"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.contribution_analysis_default_list
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.donut_options
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.pie_chart_field_wells
    import capo_quicksight.types.pie_chart_sort_configuration
    import capo_quicksight.types.small_multiples_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class PieChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.pie_chart_field_wells.PieChartFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.pie_chart_sort_configuration.PieChartSortConfiguration"
    ]
    """<p>The sort configuration of a pie chart.</p>"""
    donut_options: NotRequired["capo_quicksight.types.donut_options.DonutOptions"]
    """<p>The options that determine the shape of the chart. This option determines whether the chart is a pie chart or a donut chart.</p>"""
    small_multiples_options: NotRequired[
        "capo_quicksight.types.small_multiples_options.SmallMultiplesOptions"
    ]
    """<p>The small multiples setup for the visual.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the group/color that is displayed in a pie chart.</p>"""
    value_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options for the value that is displayed in a pie chart.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    contribution_analysis_defaults: NotRequired[
        "capo_quicksight.types.contribution_analysis_default_list.ContributionAnalysisDefaultList"
    ]
    """<p>The contribution analysis (anomaly configuration) setup of the visual.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.pie_chart_field_wells

        out["FieldWells"] = capo_quicksight.types.pie_chart_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.pie_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.pie_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "donut_options" in value:
        import capo_quicksight.types.donut_options

        out["DonutOptions"] = capo_quicksight.types.donut_options.serialize_json(
            value["donut_options"]
        )
    if "small_multiples_options" in value:
        import capo_quicksight.types.small_multiples_options

        out["SmallMultiplesOptions"] = (
            capo_quicksight.types.small_multiples_options.serialize_json(
                value["small_multiples_options"]
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


def deserialize_json(data: dict) -> PieChartConfiguration:
    out: PieChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.pie_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.pie_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.pie_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.pie_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("DonutOptions") is not None:
        import capo_quicksight.types.donut_options

        out["donut_options"] = capo_quicksight.types.donut_options.deserialize_json(
            data["DonutOptions"]
        )
    if data.get("SmallMultiplesOptions") is not None:
        import capo_quicksight.types.small_multiples_options

        out["small_multiples_options"] = (
            capo_quicksight.types.small_multiples_options.deserialize_json(
                data["SmallMultiplesOptions"]
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


def redact_sensitive(value: PieChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.pie_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.pie_chart_field_wells.redact_sensitive(
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
