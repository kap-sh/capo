"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HealthStatusFilter``."""

from typing import Literal, TypeAlias, cast

HealthStatusFilter: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "ALL",
    "HEALTHY_OR_ELSE_ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatusFilter:
    return cast(HealthStatusFilter, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HealthStatusFilter) -> str:
    return value


def deserialize_cbor(data: str) -> HealthStatusFilter:
    return cast(HealthStatusFilter, data)
