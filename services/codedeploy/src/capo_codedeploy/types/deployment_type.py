"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentType``."""

from typing import Literal, TypeAlias, cast

DeploymentType: TypeAlias = Literal[
    "IN_PLACE",
    "BLUE_GREEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentType:
    return cast(DeploymentType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentType) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentType:
    return cast(DeploymentType, data)
