"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicColumns``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_column

TopicColumns: TypeAlias = list["capo_quicksight.types.topic_column.TopicColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: TopicColumns) -> list:
    import capo_quicksight.types.topic_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicColumns:
    import capo_quicksight.types.topic_column

    out: TopicColumns = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_column.deserialize_json(item))
    return out


def redact_sensitive(value: TopicColumns) -> list[Any]:
    import capo_quicksight.types.topic_column

    return [capo_quicksight.types.topic_column.redact_sensitive(item) for item in value]
