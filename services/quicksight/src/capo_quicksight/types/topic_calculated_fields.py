"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCalculatedFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_calculated_field

TopicCalculatedFields: TypeAlias = list[
    "capo_quicksight.types.topic_calculated_field.TopicCalculatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicCalculatedFields) -> list:
    import capo_quicksight.types.topic_calculated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_calculated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicCalculatedFields:
    import capo_quicksight.types.topic_calculated_field

    out: TopicCalculatedFields = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_calculated_field.deserialize_json(item))
    return out


def redact_sensitive(value: TopicCalculatedFields) -> list[Any]:
    import capo_quicksight.types.topic_calculated_field

    return [
        capo_quicksight.types.topic_calculated_field.redact_sensitive(item)
        for item in value
    ]
