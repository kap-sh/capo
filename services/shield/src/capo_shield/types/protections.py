"""Generated from Smithy shape ``com.amazonaws.shield#Protections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection

Protections: TypeAlias = list["capo_shield.types.protection.Protection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protections) -> list:
    import capo_shield.types.protection

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Protections:
    import capo_shield.types.protection

    out: Protections = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protection.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Protections) -> list:
    import capo_shield.types.protection

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Protections:
    import capo_shield.types.protection

    out: Protections = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protection.deserialize_cbor(item))
    return out
