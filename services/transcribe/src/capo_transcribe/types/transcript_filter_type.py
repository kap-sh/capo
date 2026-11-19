"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptFilterType``."""

from typing import Literal, TypeAlias, cast

TranscriptFilterType: TypeAlias = Literal["EXACT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TranscriptFilterType:
    return cast(TranscriptFilterType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TranscriptFilterType) -> str:
    return value


def deserialize_cbor(data: str) -> TranscriptFilterType:
    return cast(TranscriptFilterType, data)
