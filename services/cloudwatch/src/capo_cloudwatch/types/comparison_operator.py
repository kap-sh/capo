"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

ComparisonOperator: TypeAlias = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanLowerOrGreaterThanUpperThreshold",
    "LessThanLowerThreshold",
    "GreaterThanUpperThreshold",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)


# --- awsQuery ser/de ---
def to_query_text(value: ComparisonOperator) -> str:
    return value


def from_query_text(text: str) -> ComparisonOperator:
    return cast(ComparisonOperator, text)


def serialize_query(
    value: ComparisonOperator, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ComparisonOperator:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComparisonOperator) -> str:
    return value


def deserialize_cbor(data: str) -> ComparisonOperator:
    return cast(ComparisonOperator, data)
