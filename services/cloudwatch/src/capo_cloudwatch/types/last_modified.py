"""Generated from Smithy shape ``com.amazonaws.cloudwatch#LastModified``."""

import datetime
from typing import TypeAlias

from capo_cloudwatch._protocol.xml import Element

LastModified: TypeAlias = datetime.datetime


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastModified) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_aws_json_1_0(data: float) -> LastModified:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)


# --- awsQuery ser/de ---
def to_query_text(value: LastModified) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def from_query_text(text: str) -> LastModified:
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


def serialize_query(
    value: LastModified, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LastModified:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastModified) -> LastModified:
    return value


def deserialize_cbor(data: LastModified) -> LastModified:
    return data
