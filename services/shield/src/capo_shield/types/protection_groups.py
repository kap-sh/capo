"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.protection_group

ProtectionGroups: TypeAlias = list["capo_shield.types.protection_group.ProtectionGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroups) -> list:
    import capo_shield.types.protection_group

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectionGroups:
    import capo_shield.types.protection_group

    out: ProtectionGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protection_group.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroups) -> list:
    import capo_shield.types.protection_group

    out: list = []
    for item in value:
        out.append(capo_shield.types.protection_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtectionGroups:
    import capo_shield.types.protection_group

    out: ProtectionGroups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.protection_group.deserialize_cbor(item))
    return out
