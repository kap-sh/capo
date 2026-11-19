"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StateValue``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

StateValue: TypeAlias = Literal[
    "OK",
    "ALARM",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateValue:
    return cast(StateValue, data)


# --- awsQuery ser/de ---
def to_query_text(value: StateValue) -> str:
    return value


def from_query_text(text: str) -> StateValue:
    return cast(StateValue, text)


def serialize_query(
    value: StateValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StateValue:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StateValue) -> str:
    return value


def deserialize_cbor(data: str) -> StateValue:
    return cast(StateValue, data)
