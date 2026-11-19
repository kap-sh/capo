"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Ec2AsgCapacityMonitoringApproach``."""

from typing import Literal, TypeAlias, cast

Ec2AsgCapacityMonitoringApproach: TypeAlias = Literal[
    "sampledMaxInLast24Hours",
    "autoscalingMaxInLast24Hours",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AsgCapacityMonitoringApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Ec2AsgCapacityMonitoringApproach:
    return cast(Ec2AsgCapacityMonitoringApproach, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ec2AsgCapacityMonitoringApproach) -> str:
    return value


def deserialize_cbor(data: str) -> Ec2AsgCapacityMonitoringApproach:
    return cast(Ec2AsgCapacityMonitoringApproach, data)
