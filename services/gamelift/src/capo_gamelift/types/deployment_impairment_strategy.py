"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentImpairmentStrategy``."""

from typing import Literal, TypeAlias, cast

DeploymentImpairmentStrategy: TypeAlias = Literal[
    "MAINTAIN",
    "ROLLBACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentImpairmentStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentImpairmentStrategy:
    return cast(DeploymentImpairmentStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentImpairmentStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentImpairmentStrategy:
    return cast(DeploymentImpairmentStrategy, data)
