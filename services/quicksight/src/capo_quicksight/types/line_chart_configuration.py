"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.contribution_analysis_default_list
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.forecast_configuration_list
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.line_chart_default_series_settings
    import capo_quicksight.types.line_chart_field_wells
    import capo_quicksight.types.line_chart_sort_configuration
    import capo_quicksight.types.line_chart_type
    import capo_quicksight.types.line_series_axis_display_options
    import capo_quicksight.types.reference_line_list
    import capo_quicksight.types.series_item_list
    import capo_quicksight.types.single_axis_options
    import capo_quicksight.types.small_multiples_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class LineChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.line_chart_field_wells.LineChartFieldWells"
    ]
    """<p>The field well configuration of a line chart.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.line_chart_sort_configuration.LineChartSortConfiguration"
    ]
    """<p>The sort configuration of a line chart.</p>"""
    forecast_configurations: NotRequired[
        "capo_quicksight.types.forecast_configuration_list.ForecastConfigurationList"
    ]
    """<p>The forecast configuration of a line chart.</p>"""
    type: NotRequired["capo_quicksight.types.line_chart_type.LineChartType"]
    """<p>Determines the type of the line chart.</p>"""
    small_multiples_options: NotRequired[
        "capo_quicksight.types.small_multiples_options.SmallMultiplesOptions"
    ]
    """<p>The small multiples setup for the visual.</p>"""
    x_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the x-axis.</p>"""
    x_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the x-axis label.</p>"""
    primary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.line_series_axis_display_options.LineSeriesAxisDisplayOptions"
    ]
    """<p>The series axis configuration of a line chart.</p>"""
    primary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the y-axis label.</p>"""
    secondary_y_axis_display_options: NotRequired[
        "capo_quicksight.types.line_series_axis_display_options.LineSeriesAxisDisplayOptions"
    ]
    """<p>The series axis configuration of a line chart.</p>"""
    secondary_y_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the secondary y-axis label.</p>"""
    single_axis_options: NotRequired[
        "capo_quicksight.types.single_axis_options.SingleAxisOptions"
    ]
    default_series_settings: NotRequired[
        "capo_quicksight.types.line_chart_default_series_settings.LineChartDefaultSeriesSettings"
    ]
    """<p>The options that determine the default presentation of all line series in <code>LineChartVisual</code>.</p>"""
    series: NotRequired["capo_quicksight.types.series_item_list.SeriesItemList"]
    """<p>The series item configuration of a line chart.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend configuration of a line chart.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a line chart.</p>"""
    reference_lines: NotRequired[
        "capo_quicksight.types.reference_line_list.ReferenceLineList"
    ]
    """<p>The reference lines configuration of a line chart.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a line chart.</p>"""
    contribution_analysis_defaults: NotRequired[
        "capo_quicksight.types.contribution_analysis_default_list.ContributionAnalysisDefaultList"
    ]
    """<p>The default configuration of a line chart's contribution analysis.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a line chart.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.line_chart_field_wells

        out["FieldWells"] = capo_quicksight.types.line_chart_field_wells.serialize_json(
            value["field_wells"]
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.line_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.line_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "forecast_configurations" in value:
        import capo_quicksight.types.forecast_configuration_list

        out["ForecastConfigurations"] = (
            capo_quicksight.types.forecast_configuration_list.serialize_json(
                value["forecast_configurations"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.line_chart_type

        out["Type"] = capo_quicksight.types.line_chart_type.serialize_json(
            value["type"]
        )
    if "small_multiples_options" in value:
        import capo_quicksight.types.small_multiples_options

        out["SmallMultiplesOptions"] = (
            capo_quicksight.types.small_multiples_options.serialize_json(
                value["small_multiples_options"]
            )
        )
    if "x_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["XAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["x_axis_display_options"]
            )
        )
    if "x_axis_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["XAxisLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["x_axis_label_options"]
            )
        )
    if "primary_y_axis_display_options" in value:
        import capo_quicksight.types.line_series_axis_display_options

        out["PrimaryYAxisDisplayOptions"] = (
            capo_quicksight.types.line_series_axis_display_options.serialize_json(
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
        import capo_quicksight.types.line_series_axis_display_options

        out["SecondaryYAxisDisplayOptions"] = (
            capo_quicksight.types.line_series_axis_display_options.serialize_json(
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
    if "default_series_settings" in value:
        import capo_quicksight.types.line_chart_default_series_settings

        out["DefaultSeriesSettings"] = (
            capo_quicksight.types.line_chart_default_series_settings.serialize_json(
                value["default_series_settings"]
            )
        )
    if "series" in value:
        import capo_quicksight.types.series_item_list

        out["Series"] = capo_quicksight.types.series_item_list.serialize_json(
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
    if "reference_lines" in value:
        import capo_quicksight.types.reference_line_list

        out["ReferenceLines"] = (
            capo_quicksight.types.reference_line_list.serialize_json(
                value["reference_lines"]
            )
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "contribution_analysis_defaults" in value:
        import capo_quicksight.types.contribution_analysis_default_list

        out["ContributionAnalysisDefaults"] = (
            capo_quicksight.types.contribution_analysis_default_list.serialize_json(
                value["contribution_analysis_defaults"]
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


def deserialize_json(data: dict) -> LineChartConfiguration:
    out: LineChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.line_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.line_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.line_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.line_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("ForecastConfigurations") is not None:
        import capo_quicksight.types.forecast_configuration_list

        out["forecast_configurations"] = (
            capo_quicksight.types.forecast_configuration_list.deserialize_json(
                data["ForecastConfigurations"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.line_chart_type

        out["type"] = capo_quicksight.types.line_chart_type.deserialize_json(
            data["Type"]
        )
    if data.get("SmallMultiplesOptions") is not None:
        import capo_quicksight.types.small_multiples_options

        out["small_multiples_options"] = (
            capo_quicksight.types.small_multiples_options.deserialize_json(
                data["SmallMultiplesOptions"]
            )
        )
    if data.get("XAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["x_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["XAxisDisplayOptions"]
            )
        )
    if data.get("XAxisLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["x_axis_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["XAxisLabelOptions"]
            )
        )
    if data.get("PrimaryYAxisDisplayOptions") is not None:
        import capo_quicksight.types.line_series_axis_display_options

        out["primary_y_axis_display_options"] = (
            capo_quicksight.types.line_series_axis_display_options.deserialize_json(
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
        import capo_quicksight.types.line_series_axis_display_options

        out["secondary_y_axis_display_options"] = (
            capo_quicksight.types.line_series_axis_display_options.deserialize_json(
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
    if data.get("DefaultSeriesSettings") is not None:
        import capo_quicksight.types.line_chart_default_series_settings

        out["default_series_settings"] = (
            capo_quicksight.types.line_chart_default_series_settings.deserialize_json(
                data["DefaultSeriesSettings"]
            )
        )
    if data.get("Series") is not None:
        import capo_quicksight.types.series_item_list

        out["series"] = capo_quicksight.types.series_item_list.deserialize_json(
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
    if data.get("ReferenceLines") is not None:
        import capo_quicksight.types.reference_line_list

        out["reference_lines"] = (
            capo_quicksight.types.reference_line_list.deserialize_json(
                data["ReferenceLines"]
            )
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("ContributionAnalysisDefaults") is not None:
        import capo_quicksight.types.contribution_analysis_default_list

        out["contribution_analysis_defaults"] = (
            capo_quicksight.types.contribution_analysis_default_list.deserialize_json(
                data["ContributionAnalysisDefaults"]
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


def redact_sensitive(value: LineChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.line_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.line_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "series" in value:
        import capo_quicksight.types.series_item_list

        out["series"] = capo_quicksight.types.series_item_list.redact_sensitive(
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
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
