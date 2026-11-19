"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentReadyAction``."""

from typing import Literal, TypeAlias, cast

DeploymentReadyAction: TypeAlias = Literal[
    "CONTINUE_DEPLOYMENT",
    "STOP_DEPLOYMENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentReadyAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentReadyAction:
    return cast(DeploymentReadyAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentReadyAction) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentReadyAction:
    return cast(DeploymentReadyAction, data)
