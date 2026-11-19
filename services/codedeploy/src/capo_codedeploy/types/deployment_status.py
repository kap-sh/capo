"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentStatus: TypeAlias = Literal[
    "Created",
    "Queued",
    "InProgress",
    "Baking",
    "Succeeded",
    "Failed",
    "Stopped",
    "Ready",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
