"""Generated from Smithy shape ``com.amazonaws.pi#AcceptLanguage``."""

from typing import Literal, TypeAlias, cast

AcceptLanguage: TypeAlias = Literal["EN_US",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptLanguage:
    return cast(AcceptLanguage, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptLanguage) -> str:
    return value


def deserialize_cbor(data: str) -> AcceptLanguage:
    return cast(AcceptLanguage, data)
