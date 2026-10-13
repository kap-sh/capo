"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerOverrides``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_override

ContainerOverrides: TypeAlias = list[
    "capo_ecs.types.container_override.ContainerOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerOverrides) -> list:
    import capo_ecs.types.container_override

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_override.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerOverrides:
    import capo_ecs.types.container_override

    out: ContainerOverrides = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.container_override.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ContainerOverrides) -> list[Any]:
    import capo_ecs.types.container_override

    return [capo_ecs.types.container_override.redact_sensitive(item) for item in value]
