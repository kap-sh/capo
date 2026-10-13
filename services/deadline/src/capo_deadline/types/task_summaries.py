"""Generated from Smithy shape ``com.amazonaws.deadline#TaskSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.task_summary

TaskSummaries: TypeAlias = list["capo_deadline.types.task_summary.TaskSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummaries) -> list:
    import capo_deadline.types.task_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSummaries:
    import capo_deadline.types.task_summary

    out: TaskSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.task_summary.deserialize_json(item))
    return out


def redact_sensitive(value: TaskSummaries) -> list[Any]:
    import capo_deadline.types.task_summary

    return [capo_deadline.types.task_summary.redact_sensitive(item) for item in value]
