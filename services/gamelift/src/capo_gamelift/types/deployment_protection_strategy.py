"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentProtectionStrategy``."""

from typing import Literal, TypeAlias, cast

DeploymentProtectionStrategy: TypeAlias = Literal[
    "WITH_PROTECTION",
    "IGNORE_PROTECTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentProtectionStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentProtectionStrategy:
    return cast(DeploymentProtectionStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentProtectionStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> DeploymentProtectionStrategy:
    return cast(DeploymentProtectionStrategy, data)
