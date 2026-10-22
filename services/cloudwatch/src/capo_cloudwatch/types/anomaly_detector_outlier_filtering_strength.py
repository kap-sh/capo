"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorOutlierFilteringStrength``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AnomalyDetectorOutlierFilteringStrength: TypeAlias = Literal[
    "MINIMAL",
    "MODERATE",
    "STRICT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorOutlierFilteringStrength) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorOutlierFilteringStrength:
    return cast(AnomalyDetectorOutlierFilteringStrength, data)


# --- awsQuery ser/de ---
def to_query_text(value: AnomalyDetectorOutlierFilteringStrength) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorOutlierFilteringStrength:
    return cast(AnomalyDetectorOutlierFilteringStrength, text)


def serialize_query(
    value: AnomalyDetectorOutlierFilteringStrength,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorOutlierFilteringStrength:
    return from_query_text(el.text or "")
