"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#TraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.trait

TraitList: TypeAlias = list["capo_comprehendmedical.types.trait.Trait"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TraitList) -> list:
    import capo_comprehendmedical.types.trait

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.trait.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TraitList:
    import capo_comprehendmedical.types.trait

    out: TraitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.trait.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TraitList) -> list:
    import capo_comprehendmedical.types.trait

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.trait.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TraitList:
    import capo_comprehendmedical.types.trait

    out: TraitList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.trait.deserialize_cbor(item))
    return out
