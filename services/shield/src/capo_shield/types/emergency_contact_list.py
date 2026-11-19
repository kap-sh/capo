"""Generated from Smithy shape ``com.amazonaws.shield#EmergencyContactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.emergency_contact

EmergencyContactList: TypeAlias = list[
    "capo_shield.types.emergency_contact.EmergencyContact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmergencyContactList) -> list:
    import capo_shield.types.emergency_contact

    out: list = []
    for item in value:
        out.append(capo_shield.types.emergency_contact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EmergencyContactList:
    import capo_shield.types.emergency_contact

    out: EmergencyContactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.emergency_contact.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EmergencyContactList) -> list:
    import capo_shield.types.emergency_contact

    out: list = []
    for item in value:
        out.append(capo_shield.types.emergency_contact.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EmergencyContactList:
    import capo_shield.types.emergency_contact

    out: EmergencyContactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.emergency_contact.deserialize_cbor(item))
    return out
