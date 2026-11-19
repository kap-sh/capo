"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

MetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Average",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricStatistic:
    return cast(MetricStatistic, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStatistic) -> str:
    return value


def deserialize_cbor(data: str) -> MetricStatistic:
    return cast(MetricStatistic, data)
