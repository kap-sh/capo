"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisual``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.plugin_visual_configuration
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.visual_custom_action_list
    import capo_quicksight.types.visual_subtitle_label_options
    import capo_quicksight.types.visual_title_label_options


class PluginVisual(TypedDict, closed=True):
    visual_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the visual that you want to use.</p>"""
    plugin_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that reflects the plugin and version.</p>"""
    title: NotRequired[
        "capo_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    subtitle: NotRequired[
        "capo_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    chart_configuration: NotRequired[
        "capo_quicksight.types.plugin_visual_configuration.PluginVisualConfiguration"
    ]
    """<p> A description of the plugin field wells and their persisted properties. </p>"""
    actions: NotRequired[
        "capo_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""
    visual_content_alt_text: NotRequired[
        "capo_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    out["PluginArn"] = value["plugin_arn"]
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
        import capo_quicksight.types.plugin_visual_configuration

        out["ChartConfiguration"] = (
            capo_quicksight.types.plugin_visual_configuration.serialize_json(
                value["chart_configuration"]
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


def deserialize_json(data: dict) -> PluginVisual:
    out: PluginVisual = {}  # type: ignore[typeddict-item]
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        out["visual_id"] = ""
    if data.get("PluginArn") is not None:
        out["plugin_arn"] = data["PluginArn"]
    else:
        out["plugin_arn"] = ""
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
        import capo_quicksight.types.plugin_visual_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.plugin_visual_configuration.deserialize_json(
                data["ChartConfiguration"]
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


def redact_sensitive(value: PluginVisual) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "chart_configuration" in value:
        import capo_quicksight.types.plugin_visual_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.plugin_visual_configuration.redact_sensitive(
                value["chart_configuration"]
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
