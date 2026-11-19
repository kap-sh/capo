"""Generated from Smithy shape ``com.amazonaws.transcribe#Words``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.word

Words: TypeAlias = list["capo_transcribe.types.word.Word"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Words) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Words:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Words) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Words:
    return [item for item in data if item is not None]
