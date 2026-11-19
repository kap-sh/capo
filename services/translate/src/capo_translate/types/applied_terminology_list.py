"""Generated from Smithy shape ``com.amazonaws.translate#AppliedTerminologyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_translate.types.applied_terminology

AppliedTerminologyList: TypeAlias = list[
    "capo_translate.types.applied_terminology.AppliedTerminology"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppliedTerminologyList) -> list:
    import capo_translate.types.applied_terminology

    out: list = []
    for item in value:
        out.append(
            capo_translate.types.applied_terminology.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppliedTerminologyList:
    import capo_translate.types.applied_terminology

    out: AppliedTerminologyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_translate.types.applied_terminology.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppliedTerminologyList) -> list:
    import capo_translate.types.applied_terminology

    out: list = []
    for item in value:
        out.append(capo_translate.types.applied_terminology.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AppliedTerminologyList:
    import capo_translate.types.applied_terminology

    out: AppliedTerminologyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_translate.types.applied_terminology.deserialize_cbor(item))
    return out
