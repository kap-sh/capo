"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerMonitoringType``."""

from typing import Literal, TypeAlias, cast

ContainerMonitoringType: TypeAlias = Literal[
    "ECS",
    "EKS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerMonitoringType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContainerMonitoringType:
    return cast(ContainerMonitoringType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerMonitoringType) -> str:
    return value


def deserialize_cbor(data: str) -> ContainerMonitoringType:
    return cast(ContainerMonitoringType, data)
