"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamOutputFormat``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

MetricStreamOutputFormat: TypeAlias = Literal[
    "json",
    "opentelemetry0.7",
    "opentelemetry1.0",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamOutputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricStreamOutputFormat:
    return cast(MetricStreamOutputFormat, data)


# --- awsQuery ser/de ---
def to_query_text(value: MetricStreamOutputFormat) -> str:
    return value


def from_query_text(text: str) -> MetricStreamOutputFormat:
    return cast(MetricStreamOutputFormat, text)


def serialize_query(
    value: MetricStreamOutputFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricStreamOutputFormat:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamOutputFormat) -> str:
    return value


def deserialize_cbor(data: str) -> MetricStreamOutputFormat:
    return cast(MetricStreamOutputFormat, data)
