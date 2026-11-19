"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

AlarmType: TypeAlias = Literal[
    "CompositeAlarm",
    "MetricAlarm",
    "LogAlarm",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AlarmType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmType:
    return cast(AlarmType, data)


# --- awsQuery ser/de ---
def to_query_text(value: AlarmType) -> str:
    return value


def from_query_text(text: str) -> AlarmType:
    return cast(AlarmType, text)


def serialize_query(
    value: AlarmType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AlarmType:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmType) -> str:
    return value


def deserialize_cbor(data: str) -> AlarmType:
    return cast(AlarmType, data)
