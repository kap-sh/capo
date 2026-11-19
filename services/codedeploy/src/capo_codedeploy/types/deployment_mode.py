"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

DeploymentMode: TypeAlias = Literal[
    "STANDARD",
    "RESTART",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentMode:
    return cast(DeploymentMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentMode) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentMode:
    return cast(DeploymentMode, data)
