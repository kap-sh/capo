"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDefinitions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.container_definition

ContainerDefinitions: TypeAlias = list[
    "capo_ecs.types.container_definition.ContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDefinitions) -> list:
    import capo_ecs.types.container_definition

    out: list = []
    for item in value:
        out.append(capo_ecs.types.container_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDefinitions:
    import capo_ecs.types.container_definition

    out: ContainerDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.container_definition.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ContainerDefinitions) -> list[Any]:
    import capo_ecs.types.container_definition

    return [
        capo_ecs.types.container_definition.redact_sensitive(item) for item in value
    ]
