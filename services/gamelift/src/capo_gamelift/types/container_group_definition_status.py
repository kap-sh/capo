"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerGroupDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

ContainerGroupDefinitionStatus: TypeAlias = Literal[
    "READY",
    "COPYING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerGroupDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerGroupDefinitionStatus:
    return cast(ContainerGroupDefinitionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerGroupDefinitionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerGroupDefinitionStatus:
    return cast(ContainerGroupDefinitionStatus, data)
