"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "IMPAIRED",
    "COMPLETE",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "CANCELLED",
    "PENDING",
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
