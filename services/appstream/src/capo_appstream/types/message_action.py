"""Generated from Smithy shape ``com.amazonaws.appstream#MessageAction``."""

from typing import Literal, TypeAlias, cast

MessageAction: TypeAlias = Literal[
    "SUPPRESS",
    "RESEND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MessageAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageAction:
    return cast(MessageAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MessageAction) -> str:
    return value


def deserialize_cbor(data: str) -> MessageAction:
    return cast(MessageAction, data)
