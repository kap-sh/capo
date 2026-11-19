"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_value

MetricValues: TypeAlias = list["capo_compute_optimizer.types.metric_value.MetricValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricValues) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_aws_json_1_0(data: list) -> MetricValues:
    return [float(item) for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> MetricValues:
    return [float(item) for item in data if item is not None]
