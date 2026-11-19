"""Generated from Smithy shape ``com.amazonaws.translate#Profanity``."""

from typing import Literal, TypeAlias, cast

Profanity: TypeAlias = Literal["MASK",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Profanity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Profanity:
    return cast(Profanity, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Profanity) -> str:
    return value


def deserialize_cbor(data: str) -> Profanity:
    return cast(Profanity, data)
