"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_job_item

BatchUpdateJobItems: TypeAlias = list[
    "capo_deadline.types.batch_update_job_item.BatchUpdateJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobItems) -> list:
    import capo_deadline.types.batch_update_job_item

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_update_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUpdateJobItems:
    import capo_deadline.types.batch_update_job_item

    out: BatchUpdateJobItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.batch_update_job_item.deserialize_json(item))
    return out


def redact_sensitive(value: BatchUpdateJobItems) -> list[Any]:
    import capo_deadline.types.batch_update_job_item

    return [
        capo_deadline.types.batch_update_job_item.redact_sensitive(item)
        for item in value
    ]
