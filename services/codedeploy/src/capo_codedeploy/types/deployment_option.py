"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentOption``."""

from typing import Literal, TypeAlias, cast

DeploymentOption: TypeAlias = Literal[
    "WITH_TRAFFIC_CONTROL",
    "WITHOUT_TRAFFIC_CONTROL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentOption:
    return cast(DeploymentOption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentOption) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentOption:
    return cast(DeploymentOption, data)
