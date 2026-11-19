"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_filter_info

VocabularyFilters: TypeAlias = list[
    "capo_transcribe.types.vocabulary_filter_info.VocabularyFilterInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VocabularyFilters) -> list:
    import capo_transcribe.types.vocabulary_filter_info

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.vocabulary_filter_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VocabularyFilters:
    import capo_transcribe.types.vocabulary_filter_info

    out: VocabularyFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.vocabulary_filter_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VocabularyFilters) -> list:
    import capo_transcribe.types.vocabulary_filter_info

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.vocabulary_filter_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> VocabularyFilters:
    import capo_transcribe.types.vocabulary_filter_info

    out: VocabularyFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.vocabulary_filter_info.deserialize_cbor(item))
    return out
