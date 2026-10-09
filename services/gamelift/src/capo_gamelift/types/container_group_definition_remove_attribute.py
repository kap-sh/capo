"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinitionRemoveAttribute``."""

from typing import Literal, TypeAlias, cast

ContainerGroupDefinitionRemoveAttribute: TypeAlias = Literal["TOTAL_VCPU_LIMIT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupDefinitionRemoveAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerGroupDefinitionRemoveAttribute:
    return cast(ContainerGroupDefinitionRemoveAttribute, data)
