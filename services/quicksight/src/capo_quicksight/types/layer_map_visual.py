"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerMapVisual``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.geospatial_layer_map_configuration
    import capo_quicksight.types.long_plain_text
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.topic_identifier
    import capo_quicksight.types.visual_subtitle_label_options
    import capo_quicksight.types.visual_title_label_options


class LayerMapVisual(TypedDict, closed=True):
    visual_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the visual.</p>"""
    title: NotRequired[
        "capo_quicksight.types.visual_title_label_options.VisualTitleLabelOptions"
    ]
    subtitle: NotRequired[
        "capo_quicksight.types.visual_subtitle_label_options.VisualSubtitleLabelOptions"
    ]
    chart_configuration: NotRequired[
        "capo_quicksight.types.geospatial_layer_map_configuration.GeospatialLayerMapConfiguration"
    ]
    """<p>The configuration settings of the visual.</p>"""
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The dataset that is used to create the layer map visual. You can't create a visual without a dataset or a topic.</p>"""
    topic_identifier: NotRequired[
        "capo_quicksight.types.topic_identifier.TopicIdentifier"
    ]
    """<p>The topic that is used in the layer map visual. You can't create a visual without a dataset or a topic.</p>"""
    visual_content_alt_text: NotRequired[
        "capo_quicksight.types.long_plain_text.LongPlainText"
    ]
    """<p>The alt text for the visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerMapVisual) -> dict:
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
        import capo_quicksight.types.geospatial_layer_map_configuration

        out["ChartConfiguration"] = (
            capo_quicksight.types.geospatial_layer_map_configuration.serialize_json(
                value["chart_configuration"]
            )
        )
    out["DataSetIdentifier"] = value.get("data_set_identifier", "")
    if "topic_identifier" in value:
        out["TopicIdentifier"] = value["topic_identifier"]
    if "visual_content_alt_text" in value:
        out["VisualContentAltText"] = value["visual_content_alt_text"]
    return out


def deserialize_json(data: dict) -> LayerMapVisual:
    out: LayerMapVisual = {}  # type: ignore[typeddict-item]
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("LayerMapVisual.visual_id required")
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
        import capo_quicksight.types.geospatial_layer_map_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.geospatial_layer_map_configuration.deserialize_json(
                data["ChartConfiguration"]
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


def redact_sensitive(value: LayerMapVisual) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "chart_configuration" in value:
        import capo_quicksight.types.geospatial_layer_map_configuration

        out["chart_configuration"] = (
            capo_quicksight.types.geospatial_layer_map_configuration.redact_sensitive(
                value["chart_configuration"]
            )
        )
    return out
