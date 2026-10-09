"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinitionRemoveAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.container_group_definition_remove_attribute

ContainerGroupDefinitionRemoveAttributeList: TypeAlias = list[
    "capo_gamelift.types.container_group_definition_remove_attribute.ContainerGroupDefinitionRemoveAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupDefinitionRemoveAttributeList) -> list:
    import capo_gamelift.types.container_group_definition_remove_attribute

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.container_group_definition_remove_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerGroupDefinitionRemoveAttributeList:
    import capo_gamelift.types.container_group_definition_remove_attribute

    out: ContainerGroupDefinitionRemoveAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gamelift.types.container_group_definition_remove_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
