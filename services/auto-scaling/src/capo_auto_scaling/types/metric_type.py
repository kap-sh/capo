"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricType``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

MetricType: TypeAlias = Literal[
    "ASGAverageCPUUtilization",
    "ASGAverageCPUUtilizationHighResolution",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "ALBRequestCountPerTarget",
]


# --- awsQuery ser/de ---
def to_query_text(value: MetricType) -> str:
    return value


def from_query_text(text: str) -> MetricType:
    return cast(MetricType, text)


def serialize_query(
    value: MetricType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricType:
    return from_query_text(el.text or "")
