"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_display_options
    import capo_quicksight.types.chart_axis_label_options
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.histogram_bin_options
    import capo_quicksight.types.histogram_field_wells
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class HistogramConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.histogram_field_wells.HistogramFieldWells"
    ]
    """<p>The field well configuration of a histogram.</p>"""
    x_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the x-axis.</p>"""
    x_axis_label_options: NotRequired[
        "capo_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the x-axis label.</p>"""
    y_axis_display_options: NotRequired[
        "capo_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the y-axis.</p>"""
    bin_options: NotRequired[
        "capo_quicksight.types.histogram_bin_options.HistogramBinOptions"
    ]
    """<p>The options that determine the presentation of histogram bins.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a histogram.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a histogram.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a histogram.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.histogram_field_wells

        out["FieldWells"] = capo_quicksight.types.histogram_field_wells.serialize_json(
            value["field_wells"]
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
    if "y_axis_display_options" in value:
        import capo_quicksight.types.axis_display_options

        out["YAxisDisplayOptions"] = (
            capo_quicksight.types.axis_display_options.serialize_json(
                value["y_axis_display_options"]
            )
        )
    if "bin_options" in value:
        import capo_quicksight.types.histogram_bin_options

        out["BinOptions"] = capo_quicksight.types.histogram_bin_options.serialize_json(
            value["bin_options"]
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


def deserialize_json(data: dict) -> HistogramConfiguration:
    out: HistogramConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.histogram_field_wells

        out["field_wells"] = (
            capo_quicksight.types.histogram_field_wells.deserialize_json(
                data["FieldWells"]
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
    if data.get("YAxisDisplayOptions") is not None:
        import capo_quicksight.types.axis_display_options

        out["y_axis_display_options"] = (
            capo_quicksight.types.axis_display_options.deserialize_json(
                data["YAxisDisplayOptions"]
            )
        )
    if data.get("BinOptions") is not None:
        import capo_quicksight.types.histogram_bin_options

        out["bin_options"] = (
            capo_quicksight.types.histogram_bin_options.deserialize_json(
                data["BinOptions"]
            )
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


def redact_sensitive(value: HistogramConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.histogram_field_wells

        out["field_wells"] = (
            capo_quicksight.types.histogram_field_wells.redact_sensitive(
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
