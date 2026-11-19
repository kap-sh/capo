"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricMonotonicity``."""

from typing import Literal, TypeAlias, cast

"""Describes whether a Sum is a non-negative accumulation. For a monotonic Sum, delta values are non-negative and cumulative values do not decrease except when the stream resets. A non-monotonic Sum can report positive or negative changes."""
MetricMonotonicity: TypeAlias = Literal[
    "monotonic",
    "non_monotonic",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricMonotonicity) -> str:
    return value


def deserialize_cbor(data: str) -> MetricMonotonicity:
    return cast(MetricMonotonicity, data)
