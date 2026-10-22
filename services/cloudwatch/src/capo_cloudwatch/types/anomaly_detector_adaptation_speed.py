"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorAdaptationSpeed``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AnomalyDetectorAdaptationSpeed: TypeAlias = Literal[
    "FAST",
    "NORMAL",
    "SLOW",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorAdaptationSpeed) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorAdaptationSpeed:
    return cast(AnomalyDetectorAdaptationSpeed, data)


# --- awsQuery ser/de ---
def to_query_text(value: AnomalyDetectorAdaptationSpeed) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorAdaptationSpeed:
    return cast(AnomalyDetectorAdaptationSpeed, text)


def serialize_query(
    value: AnomalyDetectorAdaptationSpeed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorAdaptationSpeed:
    return from_query_text(el.text or "")
