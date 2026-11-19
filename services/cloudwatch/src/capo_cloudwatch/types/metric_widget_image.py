"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricWidgetImage``."""

import base64
from typing import TypeAlias

from capo_cloudwatch._protocol.xml import Element

MetricWidgetImage: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricWidgetImage) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> MetricWidgetImage:
    return base64.b64decode(data)


# --- awsQuery ser/de ---
def to_query_text(value: MetricWidgetImage) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> MetricWidgetImage:
    return base64.b64decode(text)


def serialize_query(
    value: MetricWidgetImage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricWidgetImage:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricWidgetImage) -> MetricWidgetImage:
    return value


def deserialize_cbor(data: MetricWidgetImage) -> MetricWidgetImage:
    return data
