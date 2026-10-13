"""Generated from Smithy shape ``com.amazonaws.quicksight#InsightVisual``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.insight_configuration
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.topic_identifier
    import capo_quicksight.types.visual_custom_action_list
    import capo_quicksight.types.visual_subtitle_label_options
    import capo_quicksight.types.visual_title_label_options


class InsightVisual(TypedDict, closed=True):
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
    insight_configuration: NotRequired[
        "capo_quicksight.types.insight_configuration.InsightConfiguration"
    ]
    """<p>The configuration of an insight visual.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The dataset that is used in the insight visual.</p>"""
    topic_identifier: NotRequired[
        "capo_quicksight.types.topic_identifier.TopicIdentifier"
    ]
    """<p>The topic that is used in the insight visual.</p>"""
    visual_content_alt_text: NotRequired[
        "capo_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightVisual) -> dict:
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
    if "insight_configuration" in value:
        import capo_quicksight.types.insight_configuration

        out["InsightConfiguration"] = (
            capo_quicksight.types.insight_configuration.serialize_json(
                value["insight_configuration"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.visual_custom_action_list

        out["Actions"] = capo_quicksight.types.visual_custom_action_list.serialize_json(
            value["actions"]
        )
    out["DataSetIdentifier"] = value.get("data_set_identifier", "")
    if "topic_identifier" in value:
        out["TopicIdentifier"] = value["topic_identifier"]
    if "visual_content_alt_text" in value:
        out["VisualContentAltText"] = value["visual_content_alt_text"]
    return out


def deserialize_json(data: dict) -> InsightVisual:
    out: InsightVisual = {}  # type: ignore[typeddict-item]
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("InsightVisual.visual_id required")
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
    if data.get("InsightConfiguration") is not None:
        import capo_quicksight.types.insight_configuration

        out["insight_configuration"] = (
            capo_quicksight.types.insight_configuration.deserialize_json(
                data["InsightConfiguration"]
            )
        )
    if data.get("Actions") is not None:
        import capo_quicksight.types.visual_custom_action_list

        out["actions"] = (
            capo_quicksight.types.visual_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        out["data_set_identifier"] = ""
    if data.get("TopicIdentifier") is not None:
        out["topic_identifier"] = data["TopicIdentifier"]
    if data.get("VisualContentAltText") is not None:
        out["visual_content_alt_text"] = data["VisualContentAltText"]
    return out


def redact_sensitive(value: InsightVisual) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "insight_configuration" in value:
        import capo_quicksight.types.insight_configuration

        out["insight_configuration"] = (
            capo_quicksight.types.insight_configuration.redact_sensitive(
                value["insight_configuration"]
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
