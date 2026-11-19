"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricHeadroom``."""

from typing import Literal, TypeAlias, cast

CustomizableMetricHeadroom: TypeAlias = Literal[
    "PERCENT_30",
    "PERCENT_20",
    "PERCENT_10",
    "PERCENT_0",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomizableMetricHeadroom) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomizableMetricHeadroom:
    return cast(CustomizableMetricHeadroom, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomizableMetricHeadroom) -> str:
    return value


def deserialize_cbor(data: str) -> CustomizableMetricHeadroom:
    return cast(CustomizableMetricHeadroom, data)
