"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnhancedInfrastructureMetrics``."""

from typing import Literal, TypeAlias, cast

EnhancedInfrastructureMetrics: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnhancedInfrastructureMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnhancedInfrastructureMetrics:
    return cast(EnhancedInfrastructureMetrics, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnhancedInfrastructureMetrics) -> str:
    return value


def deserialize_cbor(data: str) -> EnhancedInfrastructureMetrics:
    return cast(EnhancedInfrastructureMetrics, data)
