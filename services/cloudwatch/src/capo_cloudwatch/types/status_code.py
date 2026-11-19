"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StatusCode``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

StatusCode: TypeAlias = Literal[
    "Complete",
    "InternalError",
    "PartialData",
    "Forbidden",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatusCode:
    return cast(StatusCode, data)


# --- awsQuery ser/de ---
def to_query_text(value: StatusCode) -> str:
    return value


def from_query_text(text: str) -> StatusCode:
    return cast(StatusCode, text)


def serialize_query(
    value: StatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StatusCode:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatusCode) -> str:
    return value


def deserialize_cbor(data: str) -> StatusCode:
    return cast(StatusCode, data)
