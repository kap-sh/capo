"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectContainerConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_container_configuration

ServiceConnectContainerConfigurations: TypeAlias = list[
    "capo_ecs.types.service_connect_container_configuration.ServiceConnectContainerConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectContainerConfigurations) -> list:
    import capo_ecs.types.service_connect_container_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_connect_container_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceConnectContainerConfigurations:
    import capo_ecs.types.service_connect_container_configuration

    out: ServiceConnectContainerConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.service_connect_container_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
