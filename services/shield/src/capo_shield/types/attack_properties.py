"""Generated from Smithy shape ``com.amazonaws.shield#AttackProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.attack_property

AttackProperties: TypeAlias = list["capo_shield.types.attack_property.AttackProperty"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackProperties) -> list:
    import capo_shield.types.attack_property

    out: list = []
    for item in value:
        out.append(capo_shield.types.attack_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttackProperties:
    import capo_shield.types.attack_property

    out: AttackProperties = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.attack_property.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackProperties) -> list:
    import capo_shield.types.attack_property

    out: list = []
    for item in value:
        out.append(capo_shield.types.attack_property.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AttackProperties:
    import capo_shield.types.attack_property

    out: AttackProperties = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.attack_property.deserialize_cbor(item))
    return out
