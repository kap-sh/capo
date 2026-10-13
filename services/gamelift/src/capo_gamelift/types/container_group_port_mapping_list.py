"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupPortMappingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_port_mapping

ContainerGroupPortMappingList: TypeAlias = list[
    "capo_gamelift.types.container_group_port_mapping.ContainerGroupPortMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupPortMappingList) -> list:
    import capo_gamelift.types.container_group_port_mapping

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_group_port_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerGroupPortMappingList:
    import capo_gamelift.types.container_group_port_mapping

    out: ContainerGroupPortMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_group_port_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ContainerGroupPortMappingList) -> list[Any]:
    import capo_gamelift.types.container_group_port_mapping

    return [
        capo_gamelift.types.container_group_port_mapping.redact_sensitive(item)
        for item in value
    ]
