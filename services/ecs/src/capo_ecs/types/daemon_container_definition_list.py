"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerDefinitionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_container_definition

DaemonContainerDefinitionList: TypeAlias = list[
    "capo_ecs.types.daemon_container_definition.DaemonContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonContainerDefinitionList) -> list:
    import capo_ecs.types.daemon_container_definition

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.daemon_container_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonContainerDefinitionList:
    import capo_ecs.types.daemon_container_definition

    out: DaemonContainerDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.daemon_container_definition.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: DaemonContainerDefinitionList) -> list[Any]:
    import capo_ecs.types.daemon_container_definition

    return [
        capo_ecs.types.daemon_container_definition.redact_sensitive(item)
        for item in value
    ]
