"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyState``."""

from typing import Literal, TypeAlias, cast

VocabularyState: TypeAlias = Literal[
    "PENDING",
    "READY",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VocabularyState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VocabularyState:
    return cast(VocabularyState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VocabularyState) -> str:
    return value


def deserialize_cbor(data: str) -> VocabularyState:
    return cast(VocabularyState, data)
