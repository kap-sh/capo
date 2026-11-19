"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricThreshold``."""

from typing import Literal, TypeAlias, cast

CustomizableMetricThreshold: TypeAlias = Literal[
    "P90",
    "P95",
    "P99_5",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomizableMetricThreshold) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricThreshold:
    return cast(CustomizableMetricThreshold, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomizableMetricThreshold) -> str:
    return value


def deserialize_cbor(data: str) -> CustomizableMetricThreshold:
    return cast(CustomizableMetricThreshold, data)
