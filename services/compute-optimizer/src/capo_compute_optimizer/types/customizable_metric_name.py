"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricName``."""

from typing import Literal, TypeAlias, cast

CustomizableMetricName: TypeAlias = Literal[
    "CpuUtilization",
    "MemoryUtilization",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomizableMetricName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricName:
    return cast(CustomizableMetricName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomizableMetricName) -> str:
    return value


def deserialize_cbor(data: str) -> CustomizableMetricName:
    return cast(CustomizableMetricName, data)
