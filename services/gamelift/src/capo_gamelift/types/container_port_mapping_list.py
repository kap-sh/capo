"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortMappingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_port_mapping

ContainerPortMappingList: TypeAlias = list[
    "capo_gamelift.types.container_port_mapping.ContainerPortMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortMappingList) -> list:
    import capo_gamelift.types.container_port_mapping

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_port_mapping.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerPortMappingList:
    import capo_gamelift.types.container_port_mapping

    out: ContainerPortMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_port_mapping.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: ContainerPortMappingList) -> list[Any]:
    import capo_gamelift.types.container_port_mapping

    return [
        capo_gamelift.types.container_port_mapping.redact_sensitive(item)
        for item in value
    ]
