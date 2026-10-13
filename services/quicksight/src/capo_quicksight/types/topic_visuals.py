"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicVisuals``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_visual

TopicVisuals: TypeAlias = list["capo_quicksight.types.topic_visual.TopicVisual"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicVisuals) -> list:
    import capo_quicksight.types.topic_visual

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicVisuals:
    import capo_quicksight.types.topic_visual

    out: TopicVisuals = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_visual.deserialize_json(item))
    return out


def redact_sensitive(value: TopicVisuals) -> list[Any]:
    import capo_quicksight.types.topic_visual

    return [capo_quicksight.types.topic_visual.redact_sensitive(item) for item in value]
