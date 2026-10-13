"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.radar_chart_axes_range_scale
    import capo_quicksight.types.radar_chart_field_wells
    import capo_quicksight.types.radar_chart_series_settings
    import capo_quicksight.types.radar_chart_shape
    import capo_quicksight.types.radar_chart_sort_configuration
    import capo_quicksight.types.radar_chart_start_angle
    import capo_quicksight.types.visibility
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class RadarChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.radar_chart_field_wells.RadarChartFieldWells"
    ]
    """<p>The field well configuration of a <code>RadarChartVisual</code>.</p>"""
    sort_configuration: NotRequired[
        "capo_quicksight.types.radar_chart_sort_configuration.RadarChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>RadarChartVisual</code>.</p>"""
    shape: NotRequired["capo_quicksight.types.radar_chart_shape.RadarChartShape"]
    """<p>The shape of the radar chart.</p>"""
    base_series_settings: NotRequired[
        "capo_quicksight.types.radar_chart_series_settings.RadarChartSeriesSettings"
    ]
    """<p>The base sreies settings of a radar chart.</p>"""
    start_angle: NotRequired[
        "capo_quicksight.types.radar_chart_start_angle.RadarChartStartAngle"
    ]
    """<p>The start angle of a radar chart's axis.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    alternate_band_colors_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the colors of alternatign bands in a radar chart.</p>"""
    alternate_band_even_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the even-numbered alternate bands of a radar chart.</p>"""
    alternate_band_odd_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the odd-numbered alternate bands of a radar chart.</p>"""
    category_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The category axis of a radar chart.</p>"""
    category_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The category label options of a radar chart.</p>"""
    color_axis: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The color axis of a radar chart.</p>"""
    color_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The color label options of a radar chart.</p>"""
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    axes_range_scale: NotRequired[
        "capo_quicksight.types.radar_chart_axes_range_scale.RadarChartAxesRangeScale"
    ]
    """<p>The axis behavior options of a radar chart.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.radar_chart_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.radar_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import capo_quicksight.types.radar_chart_sort_configuration

        out["SortConfiguration"] = (
            capo_quicksight.types.radar_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "shape" in value:
        import capo_quicksight.types.radar_chart_shape

        out["Shape"] = capo_quicksight.types.radar_chart_shape.serialize_json(
            value["shape"]
        )
    if "base_series_settings" in value:
        import capo_quicksight.types.radar_chart_series_settings

        out["BaseSeriesSettings"] = (
            capo_quicksight.types.radar_chart_series_settings.serialize_json(
                value["base_series_settings"]
            )
        )
    if "start_angle" in value:
        out["StartAngle"] = (
            "NaN"
            if value["start_angle"] != value["start_angle"]
            else "Infinity"
            if value["start_angle"] == float("inf")
            else "-Infinity"
            if value["start_angle"] == float("-inf")
            else value["start_angle"]
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "alternate_band_colors_visibility" in value:
        import capo_quicksight.types.visibility

        out["AlternateBandColorsVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["alternate_band_colors_visibility"]
            )
        )
    if "alternate_band_even_color" in value:
        out["AlternateBandEvenColor"] = value["alternate_band_even_color"]
    if "alternate_band_odd_color" in value:
        out["AlternateBandOddColor"] = value["alternate_band_odd_color"]
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
    if "color_axis" in value:
        import capo_quicksight.types.axis_display_options

        out["ColorAxis"] = capo_quicksight.types.axis_display_options.serialize_json(
            value["color_axis"]
        )
    if "color_label_options" in value:
        import capo_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            capo_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
            )
        )
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "axes_range_scale" in value:
        import capo_quicksight.types.radar_chart_axes_range_scale

        out["AxesRangeScale"] = (
            capo_quicksight.types.radar_chart_axes_range_scale.serialize_json(
                value["axes_range_scale"]
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


def deserialize_json(data: dict) -> RadarChartConfiguration:
    out: RadarChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.radar_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.radar_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("SortConfiguration") is not None:
        import capo_quicksight.types.radar_chart_sort_configuration

        out["sort_configuration"] = (
            capo_quicksight.types.radar_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if data.get("Shape") is not None:
        import capo_quicksight.types.radar_chart_shape

        out["shape"] = capo_quicksight.types.radar_chart_shape.deserialize_json(
            data["Shape"]
        )
    if data.get("BaseSeriesSettings") is not None:
        import capo_quicksight.types.radar_chart_series_settings

        out["base_series_settings"] = (
            capo_quicksight.types.radar_chart_series_settings.deserialize_json(
                data["BaseSeriesSettings"]
            )
        )
    if data.get("StartAngle") is not None:
        out["start_angle"] = float(data["StartAngle"])
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("AlternateBandColorsVisibility") is not None:
        import capo_quicksight.types.visibility

        out["alternate_band_colors_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["AlternateBandColorsVisibility"]
            )
        )
    if data.get("AlternateBandEvenColor") is not None:
        out["alternate_band_even_color"] = data["AlternateBandEvenColor"]
    if data.get("AlternateBandOddColor") is not None:
        out["alternate_band_odd_color"] = data["AlternateBandOddColor"]
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
    if data.get("ColorAxis") is not None:
        import capo_quicksight.types.axis_display_options

        out["color_axis"] = capo_quicksight.types.axis_display_options.deserialize_json(
            data["ColorAxis"]
        )
    if data.get("ColorLabelOptions") is not None:
        import capo_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            capo_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
            )
        )
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if data.get("AxesRangeScale") is not None:
        import capo_quicksight.types.radar_chart_axes_range_scale

        out["axes_range_scale"] = (
            capo_quicksight.types.radar_chart_axes_range_scale.deserialize_json(
                data["AxesRangeScale"]
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


def redact_sensitive(value: RadarChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.radar_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.radar_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.redact_sensitive(
            value["visual_palette"]
        )
    return out
