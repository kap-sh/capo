"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerDependencyCondition``."""

from typing import Literal, TypeAlias, cast

ContainerDependencyCondition: TypeAlias = Literal[
    "START",
    "COMPLETE",
    "SUCCESS",
    "HEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependencyCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerDependencyCondition:
    return cast(ContainerDependencyCondition, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerDependencyCondition) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerDependencyCondition:
    return cast(ContainerDependencyCondition, data)
