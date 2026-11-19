"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ScanBy``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

ScanBy: TypeAlias = Literal[
    "TimestampDescending",
    "TimestampAscending",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScanBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScanBy:
    return cast(ScanBy, data)


# --- awsQuery ser/de ---
def to_query_text(value: ScanBy) -> str:
    return value


def from_query_text(text: str) -> ScanBy:
    return cast(ScanBy, text)


def serialize_query(value: ScanBy, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScanBy:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScanBy) -> str:
    return value


def deserialize_cbor(data: str) -> ScanBy:
    return cast(ScanBy, data)
