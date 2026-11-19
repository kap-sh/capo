"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AnomalyDetectorType: TypeAlias = Literal[
    "SINGLE_METRIC",
    "METRIC_MATH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorType:
    return cast(AnomalyDetectorType, data)


# --- awsQuery ser/de ---
def to_query_text(value: AnomalyDetectorType) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorType:
    return cast(AnomalyDetectorType, text)


def serialize_query(
    value: AnomalyDetectorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorType:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnomalyDetectorType) -> str:
    return value


def deserialize_cbor(data: str) -> AnomalyDetectorType:
    return cast(AnomalyDetectorType, data)
