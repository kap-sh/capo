"""Generated from Smithy shape ``com.amazonaws.shield#AttackVectorDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.attack_vector_description

AttackVectorDescriptionList: TypeAlias = list[
    "capo_shield.types.attack_vector_description.AttackVectorDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVectorDescriptionList) -> list:
    import capo_shield.types.attack_vector_description

    out: list = []
    for item in value:
        out.append(
            capo_shield.types.attack_vector_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttackVectorDescriptionList:
    import capo_shield.types.attack_vector_description

    out: AttackVectorDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_shield.types.attack_vector_description.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackVectorDescriptionList) -> list:
    import capo_shield.types.attack_vector_description

    out: list = []
    for item in value:
        out.append(capo_shield.types.attack_vector_description.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AttackVectorDescriptionList:
    import capo_shield.types.attack_vector_description

    out: AttackVectorDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.attack_vector_description.deserialize_cbor(item))
    return out
