"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthStatus``."""

from typing import Literal, TypeAlias, cast

HealthStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatus:
    return cast(HealthStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HealthStatus) -> str:
    return value


def deserialize_cbor(data: str) -> HealthStatus:
    return cast(HealthStatus, data)
