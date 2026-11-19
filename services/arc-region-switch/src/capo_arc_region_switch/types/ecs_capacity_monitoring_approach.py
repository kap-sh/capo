"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EcsCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

EcsCapacityMonitoringApproach: TypeAlias = Literal[
    "sampledMaxInLast24Hours",
    "containerInsightsMaxInLast24Hours",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EcsCapacityMonitoringApproach:
    return cast(EcsCapacityMonitoringApproach, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EcsCapacityMonitoringApproach) -> str:
    return value


def deserialize_cbor(data: str) -> EcsCapacityMonitoringApproach:
    return cast(EcsCapacityMonitoringApproach, data)
