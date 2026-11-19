"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Route53HealthCheckStatus``."""

from typing import Literal, TypeAlias, cast

Route53HealthCheckStatus: TypeAlias = Literal[
    "healthy",
    "unhealthy",
    "unknown",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53HealthCheckStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Route53HealthCheckStatus:
    return cast(Route53HealthCheckStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Route53HealthCheckStatus) -> str:
    return value


def deserialize_cbor(data: str) -> Route53HealthCheckStatus:
    return cast(Route53HealthCheckStatus, data)
