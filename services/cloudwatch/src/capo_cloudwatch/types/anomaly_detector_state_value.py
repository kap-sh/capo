"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorStateValue``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AnomalyDetectorStateValue: TypeAlias = Literal[
    "PENDING_TRAINING",
    "TRAINED_INSUFFICIENT_DATA",
    "TRAINED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnomalyDetectorStateValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorStateValue:
    return cast(AnomalyDetectorStateValue, data)


# --- awsQuery ser/de ---
def to_query_text(value: AnomalyDetectorStateValue) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorStateValue:
    return cast(AnomalyDetectorStateValue, text)


def serialize_query(
    value: AnomalyDetectorStateValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorStateValue:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnomalyDetectorStateValue) -> str:
    return value


def deserialize_cbor(data: str) -> AnomalyDetectorStateValue:
    return cast(AnomalyDetectorStateValue, data)
