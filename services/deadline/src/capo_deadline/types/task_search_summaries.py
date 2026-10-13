"""Generated from Smithy shape ``com.amazonaws.deadline#TaskSearchSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.task_search_summary

TaskSearchSummaries: TypeAlias = list[
    "capo_deadline.types.task_search_summary.TaskSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSearchSummaries) -> list:
    import capo_deadline.types.task_search_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.task_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSearchSummaries:
    import capo_deadline.types.task_search_summary

    out: TaskSearchSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.task_search_summary.deserialize_json(item))
    return out


def redact_sensitive(value: TaskSearchSummaries) -> list[Any]:
    import capo_deadline.types.task_search_summary

    return [
        capo_deadline.types.task_search_summary.redact_sensitive(item) for item in value
    ]
