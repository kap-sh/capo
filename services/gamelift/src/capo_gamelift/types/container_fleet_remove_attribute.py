"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerFleetRemoveAttribute``."""

from typing import Literal, TypeAlias, cast

ContainerFleetRemoveAttribute: TypeAlias = Literal[
    "PER_INSTANCE_CONTAINER_GROUP_DEFINITION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerFleetRemoveAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerFleetRemoveAttribute:
    return cast(ContainerFleetRemoveAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerFleetRemoveAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerFleetRemoveAttribute:
    return cast(ContainerFleetRemoveAttribute, data)
