"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNamedEntities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_named_entity

TopicNamedEntities: TypeAlias = list[
    "capo_quicksight.types.topic_named_entity.TopicNamedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicNamedEntities) -> list:
    import capo_quicksight.types.topic_named_entity

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_named_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicNamedEntities:
    import capo_quicksight.types.topic_named_entity

    out: TopicNamedEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_named_entity.deserialize_json(item))
    return out


def redact_sensitive(value: TopicNamedEntities) -> list[Any]:
    import capo_quicksight.types.topic_named_entity

    return [
        capo_quicksight.types.topic_named_entity.redact_sensitive(item)
        for item in value
    ]
