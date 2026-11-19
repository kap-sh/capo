"""Generated from Smithy shape ``com.amazonaws.mailmanager#MailFrom``."""

from typing import Literal, TypeAlias, cast

MailFrom: TypeAlias = Literal[
    "REPLACE",
    "PRESERVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MailFrom) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MailFrom:
    return cast(MailFrom, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MailFrom) -> str:
    return value


def deserialize_cbor(data: str) -> MailFrom:
    return cast(MailFrom, data)
