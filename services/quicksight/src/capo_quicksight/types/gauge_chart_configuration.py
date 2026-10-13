"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_label_options
    import capo_quicksight.types.gauge_chart_color_configuration
    import capo_quicksight.types.gauge_chart_field_wells
    import capo_quicksight.types.gauge_chart_options
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visual_interaction_options
    import capo_quicksight.types.visual_palette


class GaugeChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "capo_quicksight.types.gauge_chart_field_wells.GaugeChartFieldWells"
    ]
    """<p>The field well configuration of a <code>GaugeChartVisual</code>.</p>"""
    gauge_chart_options: NotRequired[
        "capo_quicksight.types.gauge_chart_options.GaugeChartOptions"
    ]
    """<p>The options that determine the presentation of the <code>GaugeChartVisual</code>.</p>"""
    data_labels: NotRequired[
        "capo_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a <code>GaugeChartVisual</code>.</p>"""
    tooltip_options: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a <code>GaugeChartVisual</code>.</p>"""
    visual_palette: NotRequired["capo_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a <code>GaugeChartVisual</code>.</p>"""
    color_configuration: NotRequired[
        "capo_quicksight.types.gauge_chart_color_configuration.GaugeChartColorConfiguration"
    ]
    """<p>The color configuration of a <code>GaugeChartVisual</code>.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import capo_quicksight.types.gauge_chart_field_wells

        out["FieldWells"] = (
            capo_quicksight.types.gauge_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "gauge_chart_options" in value:
        import capo_quicksight.types.gauge_chart_options

        out["GaugeChartOptions"] = (
            capo_quicksight.types.gauge_chart_options.serialize_json(
                value["gauge_chart_options"]
            )
        )
    if "data_labels" in value:
        import capo_quicksight.types.data_label_options

        out["DataLabels"] = capo_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "tooltip_options" in value:
        import capo_quicksight.types.tooltip_options

        out["TooltipOptions"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip_options"]
        )
    if "visual_palette" in value:
        import capo_quicksight.types.visual_palette

        out["VisualPalette"] = capo_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "color_configuration" in value:
        import capo_quicksight.types.gauge_chart_color_configuration

        out["ColorConfiguration"] = (
            capo_quicksight.types.gauge_chart_color_configuration.serialize_json(
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


def deserialize_json(data: dict) -> GaugeChartConfiguration:
    out: GaugeChartConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldWells") is not None:
        import capo_quicksight.types.gauge_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.gauge_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if data.get("GaugeChartOptions") is not None:
        import capo_quicksight.types.gauge_chart_options

        out["gauge_chart_options"] = (
            capo_quicksight.types.gauge_chart_options.deserialize_json(
                data["GaugeChartOptions"]
            )
        )
    if data.get("DataLabels") is not None:
        import capo_quicksight.types.data_label_options

        out["data_labels"] = capo_quicksight.types.data_label_options.deserialize_json(
            data["DataLabels"]
        )
    if data.get("TooltipOptions") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip_options"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["TooltipOptions"]
        )
    if data.get("VisualPalette") is not None:
        import capo_quicksight.types.visual_palette

        out["visual_palette"] = capo_quicksight.types.visual_palette.deserialize_json(
            data["VisualPalette"]
        )
    if data.get("ColorConfiguration") is not None:
        import capo_quicksight.types.gauge_chart_color_configuration

        out["color_configuration"] = (
            capo_quicksight.types.gauge_chart_color_configuration.deserialize_json(
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


def redact_sensitive(value: GaugeChartConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_wells" in value:
        import capo_quicksight.types.gauge_chart_field_wells

        out["field_wells"] = (
            capo_quicksight.types.gauge_chart_field_wells.redact_sensitive(
                value["field_wells"]
            )
        )
    if "gauge_chart_options" in value:
        import capo_quicksight.types.gauge_chart_options

        out["gauge_chart_options"] = (
            capo_quicksight.types.gauge_chart_options.redact_sensitive(
                value["gauge_chart_options"]
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
