"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitleFormat``."""

from typing import Literal, TypeAlias, cast

SubtitleFormat: TypeAlias = Literal[
    "vtt",
    "srt",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubtitleFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubtitleFormat:
    return cast(SubtitleFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubtitleFormat) -> str:
    return value


def deserialize_cbor(data: str) -> SubtitleFormat:
    return cast(SubtitleFormat, data)
