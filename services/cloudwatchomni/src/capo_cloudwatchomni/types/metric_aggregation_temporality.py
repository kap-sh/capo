"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricAggregationTemporality``."""

from typing import Literal, TypeAlias, cast

"""Describes how an aggregating metric reports values over time. A delta value covers the preceding reporting interval. A cumulative value covers a fixed start time through the current reporting time, restarting when the stream resets."""
MetricAggregationTemporality: TypeAlias = Literal[
    "delta",
    "cumulative",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricAggregationTemporality) -> str:
    return value


def deserialize_cbor(data: str) -> MetricAggregationTemporality:
    return cast(MetricAggregationTemporality, data)
