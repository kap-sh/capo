"""Generated from Smithy shape ``com.amazonaws.codeconnections#PublishDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

PublishDeploymentStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PublishDeploymentStatus:
    return cast(PublishDeploymentStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PublishDeploymentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PublishDeploymentStatus:
    return cast(PublishDeploymentStatus, data)
