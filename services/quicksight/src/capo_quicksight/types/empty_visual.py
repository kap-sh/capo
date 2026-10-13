"""Generated from Smithy shape ``com.amazonaws.quicksight#EmptyVisual``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_identifier
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.topic_identifier
    import capo_quicksight.types.visual_custom_action_list


class EmptyVisual(TypedDict, closed=True):
    visual_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of a visual. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have visuals with the same identifiers.</p>"""
    data_set_identifier: "capo_quicksight.types.data_set_identifier.DataSetIdentifier"
    """<p>The data set that is used in the empty visual. Every visual requires a dataset or a topic to render.</p>"""
    topic_identifier: NotRequired[
        "capo_quicksight.types.topic_identifier.TopicIdentifier"
    ]
    """<p>The topic that is used in the empty visual. Every visual requires a dataset or a topic to render.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.visual_custom_action_list.VisualCustomActionList"
    ]
    """<p>The list of custom actions that are configured for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmptyVisual) -> dict:
    out: dict = {}
    out["VisualId"] = value["visual_id"]
    out["DataSetIdentifier"] = value.get("data_set_identifier", "")
    if "topic_identifier" in value:
        out["TopicIdentifier"] = value["topic_identifier"]
    if "actions" in value:
        import capo_quicksight.types.visual_custom_action_list

        out["Actions"] = capo_quicksight.types.visual_custom_action_list.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> EmptyVisual:
    out: EmptyVisual = {}  # type: ignore[typeddict-item]
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        raise DeserializationError("EmptyVisual.visual_id required")
    if data.get("DataSetIdentifier") is not None:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        out["data_set_identifier"] = ""
    if data.get("TopicIdentifier") is not None:
        out["topic_identifier"] = data["TopicIdentifier"]
    if data.get("Actions") is not None:
        import capo_quicksight.types.visual_custom_action_list

        out["actions"] = (
            capo_quicksight.types.visual_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out


def redact_sensitive(value: EmptyVisual) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "actions" in value:
        import capo_quicksight.types.visual_custom_action_list

        out["actions"] = (
            capo_quicksight.types.visual_custom_action_list.redact_sensitive(
                value["actions"]
            )
        )
    return out
