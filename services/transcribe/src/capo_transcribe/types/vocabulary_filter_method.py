"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

VocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VocabularyFilterMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VocabularyFilterMethod:
    return cast(VocabularyFilterMethod, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VocabularyFilterMethod) -> str:
    return value


def deserialize_cbor(data: str) -> VocabularyFilterMethod:
    return cast(VocabularyFilterMethod, data)
