"""Generated from Smithy shape ``com.amazonaws.translate#TermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.term

TermList: TypeAlias = list["capo_translate.types.term.Term"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TermList) -> list:
    import capo_translate.types.term

    out: list = []
    for item in value:
        out.append(capo_translate.types.term.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TermList:
    import capo_translate.types.term

    out: TermList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_translate.types.term.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TermList) -> list:
    import capo_translate.types.term

    out: list = []
    for item in value:
        out.append(capo_translate.types.term.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TermList:
    import capo_translate.types.term

    out: TermList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_translate.types.term.deserialize_cbor(item))
    return out
