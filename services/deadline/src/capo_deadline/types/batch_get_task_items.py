"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_task_item

BatchGetTaskItems: TypeAlias = list[
    "capo_deadline.types.batch_get_task_item.BatchGetTaskItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskItems) -> list:
    import capo_deadline.types.batch_get_task_item

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_task_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetTaskItems:
    import capo_deadline.types.batch_get_task_item

    out: BatchGetTaskItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.batch_get_task_item.deserialize_json(item))
    return out


def redact_sensitive(value: BatchGetTaskItems) -> list[Any]:
    import capo_deadline.types.batch_get_task_item

    return [
        capo_deadline.types.batch_get_task_item.redact_sensitive(item) for item in value
    ]
