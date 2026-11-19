"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfKeyPhrases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.key_phrase

ListOfKeyPhrases: TypeAlias = list["capo_comprehend.types.key_phrase.KeyPhrase"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfKeyPhrases) -> list:
    import capo_comprehend.types.key_phrase

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.key_phrase.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfKeyPhrases:
    import capo_comprehend.types.key_phrase

    out: ListOfKeyPhrases = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.key_phrase.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfKeyPhrases) -> list:
    import capo_comprehend.types.key_phrase

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.key_phrase.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfKeyPhrases:
    import capo_comprehend.types.key_phrase

    out: ListOfKeyPhrases = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.key_phrase.deserialize_cbor(item))
    return out
