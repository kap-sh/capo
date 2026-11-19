"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CustomHealthStatus``."""

from typing import Literal, TypeAlias, cast

CustomHealthStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomHealthStatus:
    return cast(CustomHealthStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomHealthStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CustomHealthStatus:
    return cast(CustomHealthStatus, data)
