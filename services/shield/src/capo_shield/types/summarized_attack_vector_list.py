"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedAttackVectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.summarized_attack_vector

SummarizedAttackVectorList: TypeAlias = list[
    "capo_shield.types.summarized_attack_vector.SummarizedAttackVector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedAttackVectorList) -> list:
    import capo_shield.types.summarized_attack_vector

    out: list = []
    for item in value:
        out.append(
            capo_shield.types.summarized_attack_vector.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SummarizedAttackVectorList:
    import capo_shield.types.summarized_attack_vector

    out: SummarizedAttackVectorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.summarized_attack_vector.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummarizedAttackVectorList) -> list:
    import capo_shield.types.summarized_attack_vector

    out: list = []
    for item in value:
        out.append(capo_shield.types.summarized_attack_vector.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SummarizedAttackVectorList:
    import capo_shield.types.summarized_attack_vector

    out: SummarizedAttackVectorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.summarized_attack_vector.deserialize_cbor(item))
    return out
