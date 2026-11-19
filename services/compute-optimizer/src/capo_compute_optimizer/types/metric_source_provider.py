"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricSourceProvider``."""

from typing import Literal, TypeAlias, cast

MetricSourceProvider: TypeAlias = Literal["CloudWatchApplicationInsights",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricSourceProvider) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricSourceProvider:
    return cast(MetricSourceProvider, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricSourceProvider) -> str:
    return value


def deserialize_cbor(data: str) -> MetricSourceProvider:
    return cast(MetricSourceProvider, data)
