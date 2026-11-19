"""Generated from Smithy shape ``com.amazonaws.transcribe#StringTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.non_empty_string

StringTargetList: TypeAlias = list[
    "capo_transcribe.types.non_empty_string.NonEmptyString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringTargetList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StringTargetList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StringTargetList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> StringTargetList:
    return [item for item in data if item is not None]
