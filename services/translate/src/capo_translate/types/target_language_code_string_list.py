"""Generated from Smithy shape ``com.amazonaws.translate#TargetLanguageCodeStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.language_code_string

TargetLanguageCodeStringList: TypeAlias = list[
    "capo_translate.types.language_code_string.LanguageCodeString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetLanguageCodeStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetLanguageCodeStringList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetLanguageCodeStringList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> TargetLanguageCodeStringList:
    return [item for item in data if item is not None]
