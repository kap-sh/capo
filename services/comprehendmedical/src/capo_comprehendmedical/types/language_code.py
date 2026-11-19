"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#LanguageCode``."""

from typing import Literal, TypeAlias, cast

LanguageCode: TypeAlias = Literal["en",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LanguageCode:
    return cast(LanguageCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageCode) -> str:
    return value


def deserialize_cbor(data: str) -> LanguageCode:
    return cast(LanguageCode, data)
