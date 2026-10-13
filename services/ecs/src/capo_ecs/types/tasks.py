"""Generated from Smithy shape ``com.amazonaws.ecs#Tasks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.task

Tasks: TypeAlias = list["capo_ecs.types.task.Task"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tasks) -> list:
    import capo_ecs.types.task

    out: list = []
    for item in value:
        out.append(capo_ecs.types.task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tasks:
    import capo_ecs.types.task

    out: Tasks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.task.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Tasks) -> list[Any]:
    import capo_ecs.types.task

    return [capo_ecs.types.task.redact_sensitive(item) for item in value]
