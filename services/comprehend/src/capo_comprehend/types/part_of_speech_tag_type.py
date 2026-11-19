"""Generated from Smithy shape ``com.amazonaws.comprehend#PartOfSpeechTagType``."""

from typing import Literal, TypeAlias, cast

PartOfSpeechTagType: TypeAlias = Literal[
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CONJ",
    "CCONJ",
    "DET",
    "INTJ",
    "NOUN",
    "NUM",
    "O",
    "PART",
    "PRON",
    "PROPN",
    "PUNCT",
    "SCONJ",
    "SYM",
    "VERB",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartOfSpeechTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartOfSpeechTagType:
    return cast(PartOfSpeechTagType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartOfSpeechTagType) -> str:
    return value


def deserialize_cbor(data: str) -> PartOfSpeechTagType:
    return cast(PartOfSpeechTagType, data)
