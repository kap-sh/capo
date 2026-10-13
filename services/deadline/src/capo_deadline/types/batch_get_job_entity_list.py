"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.job_entity

BatchGetJobEntityList: TypeAlias = list["capo_deadline.types.job_entity.JobEntity"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityList) -> list:
    import capo_deadline.types.job_entity

    out: list = []
    for item in value:
        out.append(capo_deadline.types.job_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobEntityList:
    import capo_deadline.types.job_entity

    out: BatchGetJobEntityList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.job_entity.deserialize_json(item))
    return out


def redact_sensitive(value: BatchGetJobEntityList) -> list[Any]:
    import capo_deadline.types.job_entity

    return [capo_deadline.types.job_entity.redact_sensitive(item) for item in value]
