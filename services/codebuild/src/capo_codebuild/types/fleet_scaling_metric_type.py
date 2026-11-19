"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetScalingMetricType``."""

from typing import Literal, TypeAlias, cast

FleetScalingMetricType: TypeAlias = Literal["FLEET_UTILIZATION_RATE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetScalingMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetScalingMetricType:
    return cast(FleetScalingMetricType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetScalingMetricType) -> str:
    return value


def deserialize_cbor(data: str) -> FleetScalingMetricType:
    return cast(FleetScalingMetricType, data)
