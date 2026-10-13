"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartVisual``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.gauge_chart_conditional_formatting
    import capo_quicksight.types.gauge_chart_configuration
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.visual_custom_action_list
    import capo_quicksight.types.visual_subtitle_label_options
    import capo_quicksight.types.visual_title_label_options


class GaugeChartVisual(TypedDict, closed=True):
    visual_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.</p>"""
    title: NotRequired[
        "capo_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    """<p>The title that is displayed on the visual.</p>"""
    subtitle: NotRequired[
        "capo_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    """<p>The subtitle that is displayed on the visual.</p>"""
    chart_configuration: NotRequired[
        "capo_quicksight.types.gauge_chart_configuration.GaugeChartConfiguration"
    ]
    """<p>The configuration of a <code>GaugeChartVisual</code>.</p>"""
    conditional_formatting: NotRequired[
        "capo_quicksight.types.gauge_chart_conditional_formatting.GaugeChartConditionalFormatting"
    ]
    """<p>The conditional formatting of a <code>GaugeChartVisual</code>.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""
    visual_content_alt_text: NotRequired[
        "capo_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    if "title" in value:
        import capo_quicksight.types.visual_title_label_options

        out["Title"] = capo_quicksight.types.visual_title_label_options.serialize_json(
            value["title"]
        )
    if "subtitle" in value:
        import capo_quicksight.types.visual_subtitle_label_options

        out["Subtitle"] = (
            capo_quicksight.types.visual_subtitle_label_options.serialize_json(
                value["subtitle"]
            )
        )
    if "chart_configuration" in value:
        import capo_quicksight.types.gauge_chart_configuration

        out["ChartConfiguration"] = (
            capo_quicksight.types.gauge_chart_configuration.serialize_json(
                value["chart_configuration"]
            )
        )
    if "conditional_formatting" in value:
        import capo_quicksight.types.gauge_chart_conditional_formatting

        out["ConditionalFormatting"] = (
            capo_quicksight.types.gauge_chart_conditional_formatting.serialize_json(
                value["conditional_formatting"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.visual_custom_action_list

        out["Actions"] = capo_quicksight.types.visual_custom_action_list.serialize_json(
            value["actions"]
        )
    if "visual_content_alt_text" in value:
        out["VisualContentAltText"] = value["visual_content_alt_text"]
    return out


def deserialize_json(data: dict) -> GaugeChartVisual:
    out: GaugeChartVisual = {}  # type: ignore[typeddict-item]
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("GaugeChartVisual.visual_id required")
    if data.get("Title") is not None:
        import capo_quicksight.types.visual_title_label_options

        out["title"] = (
            capo_quicksight.types.visual_title_label_options.deserialize_json(
                data["Title"]
            )
        )
    if data.get("Subtitle") is not None:
        import capo_quicksight.types.visual_subtitle_label_options

        out["subtitle"] = (
            capo_quicksight.types.visual_subtitle_label_options.deserialize_json(
                data["Subtitle"]
            )
        )
    if data.get("ChartConfiguration") is not None:
        import capo_quicksight.types.gauge_chart_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.gauge_chart_configuration.deserialize_json(
                data["ChartConfiguration"]
            )
        )
    if data.get("ConditionalFormatting") is not None:
        import capo_quicksight.types.gauge_chart_conditional_formatting

        out["conditional_formatting"] = (
            capo_quicksight.types.gauge_chart_conditional_formatting.deserialize_json(
                data["ConditionalFormatting"]
            )
        )
    if data.get("Actions") is not None:
        import capo_quicksight.types.visual_custom_action_list

        out["actions"] = (
            capo_quicksight.types.visual_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    if data.get("VisualContentAltText") is not None:
        out["visual_content_alt_text"] = data["VisualContentAltText"]
    return out


def redact_sensitive(value: GaugeChartVisual) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "chart_configuration" in value:
        import capo_quicksight.types.gauge_chart_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.gauge_chart_configuration.redact_sensitive(
                value["chart_configuration"]
            )
        )
    if "conditional_formatting" in value:
        import capo_quicksight.types.gauge_chart_conditional_formatting

        out["conditional_formatting"] = (
            capo_quicksight.types.gauge_chart_conditional_formatting.redact_sensitive(
                value["conditional_formatting"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.visual_custom_action_list

        out["actions"] = (
            capo_quicksight.types.visual_custom_action_list.redact_sensitive(
                value["actions"]
            )
        )
    return out
