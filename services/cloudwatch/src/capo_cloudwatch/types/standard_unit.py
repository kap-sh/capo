"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StandardUnit``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

StandardUnit: TypeAlias = Literal[
    "Seconds",
    "Microseconds",
    "Milliseconds",
    "Bytes",
    "Kilobytes",
    "Megabytes",
    "Gigabytes",
    "Terabytes",
    "Bits",
    "Kilobits",
    "Megabits",
    "Gigabits",
    "Terabits",
    "Percent",
    "Count",
    "Bytes/Second",
    "Kilobytes/Second",
    "Megabytes/Second",
    "Gigabytes/Second",
    "Terabytes/Second",
    "Bits/Second",
    "Kilobits/Second",
    "Megabits/Second",
    "Gigabits/Second",
    "Terabits/Second",
    "Count/Second",
    "None",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StandardUnit) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StandardUnit:
    return cast(StandardUnit, data)


# --- awsQuery ser/de ---
def to_query_text(value: StandardUnit) -> str:
    return value


def from_query_text(text: str) -> StandardUnit:
    return cast(StandardUnit, text)


def serialize_query(
    value: StandardUnit, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StandardUnit:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StandardUnit) -> str:
    return value


def deserialize_cbor(data: str) -> StandardUnit:
    return cast(StandardUnit, data)
