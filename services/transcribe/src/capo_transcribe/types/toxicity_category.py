"""Generated from Smithy shape ``com.amazonaws.transcribe#ToxicityCategory``."""

from typing import Literal, TypeAlias, cast

ToxicityCategory: TypeAlias = Literal["ALL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ToxicityCategory:
    return cast(ToxicityCategory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ToxicityCategory) -> str:
    return value


def deserialize_cbor(data: str) -> ToxicityCategory:
    return cast(ToxicityCategory, data)
