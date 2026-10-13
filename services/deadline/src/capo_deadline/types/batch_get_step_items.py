"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetStepItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_step_item

BatchGetStepItems: TypeAlias = list[
    "capo_deadline.types.batch_get_step_item.BatchGetStepItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetStepItems) -> list:
    import capo_deadline.types.batch_get_step_item

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_step_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetStepItems:
    import capo_deadline.types.batch_get_step_item

    out: BatchGetStepItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.batch_get_step_item.deserialize_json(item))
    return out


def redact_sensitive(value: BatchGetStepItems) -> list[Any]:
    import capo_deadline.types.batch_get_step_item

    return [
        capo_deadline.types.batch_get_step_item.redact_sensitive(item) for item in value
    ]
