"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_action_item

BatchGetSessionActionItems: TypeAlias = list[
    "capo_deadline.types.batch_get_session_action_item.BatchGetSessionActionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionItems) -> list:
    import capo_deadline.types.batch_get_session_action_item

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.batch_get_session_action_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetSessionActionItems:
    import capo_deadline.types.batch_get_session_action_item

    out: BatchGetSessionActionItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_deadline.types.batch_get_session_action_item.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchGetSessionActionItems) -> list[Any]:
    import capo_deadline.types.batch_get_session_action_item

    return [
        capo_deadline.types.batch_get_session_action_item.redact_sensitive(item)
        for item in value
    ]
