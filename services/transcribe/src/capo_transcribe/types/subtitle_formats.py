"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitleFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.subtitle_format

SubtitleFormats: TypeAlias = list[
    "capo_transcribe.types.subtitle_format.SubtitleFormat"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubtitleFormats) -> list:
    import capo_transcribe.types.subtitle_format

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.subtitle_format.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubtitleFormats:
    import capo_transcribe.types.subtitle_format

    out: SubtitleFormats = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.subtitle_format.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubtitleFormats) -> list:
    import capo_transcribe.types.subtitle_format

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.subtitle_format.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SubtitleFormats:
    import capo_transcribe.types.subtitle_format

    out: SubtitleFormats = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.subtitle_format.deserialize_cbor(item))
    return out
