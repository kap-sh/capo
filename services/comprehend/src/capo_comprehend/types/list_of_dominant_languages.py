"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDominantLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.dominant_language

ListOfDominantLanguages: TypeAlias = list[
    "capo_comprehend.types.dominant_language.DominantLanguage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDominantLanguages) -> list:
    import capo_comprehend.types.dominant_language

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.dominant_language.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDominantLanguages:
    import capo_comprehend.types.dominant_language

    out: ListOfDominantLanguages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.dominant_language.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfDominantLanguages) -> list:
    import capo_comprehend.types.dominant_language

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.dominant_language.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfDominantLanguages:
    import capo_comprehend.types.dominant_language

    out: ListOfDominantLanguages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.dominant_language.deserialize_cbor(item))
    return out
