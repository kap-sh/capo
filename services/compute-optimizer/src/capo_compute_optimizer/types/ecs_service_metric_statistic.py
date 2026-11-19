"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceMetricStatistic``."""

from typing import Literal, TypeAlias, cast

ECSServiceMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Average",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceMetricStatistic:
    return cast(ECSServiceMetricStatistic, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceMetricStatistic) -> str:
    return value


def deserialize_cbor(data: str) -> ECSServiceMetricStatistic:
    return cast(ECSServiceMetricStatistic, data)
