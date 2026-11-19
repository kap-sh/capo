"""Generated from Smithy shape ``com.amazonaws.translate#LanguageCodeStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.language_code_string

LanguageCodeStringList: TypeAlias = list[
    "capo_translate.types.language_code_string.LanguageCodeString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageCodeStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LanguageCodeStringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LanguageCodeStringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> LanguageCodeStringList:
    return [item for item in data if item is not None]
