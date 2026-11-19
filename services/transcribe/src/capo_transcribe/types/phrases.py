"""Generated from Smithy shape ``com.amazonaws.transcribe#Phrases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.phrase

Phrases: TypeAlias = list["capo_transcribe.types.phrase.Phrase"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Phrases) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Phrases:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Phrases) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Phrases:
    return [item for item in data if item is not None]
