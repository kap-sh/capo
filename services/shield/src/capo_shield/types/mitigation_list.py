"""Generated from Smithy shape ``com.amazonaws.shield#MitigationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.mitigation

MitigationList: TypeAlias = list["capo_shield.types.mitigation.Mitigation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MitigationList) -> list:
    import capo_shield.types.mitigation

    out: list = []
    for item in value:
        out.append(capo_shield.types.mitigation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MitigationList:
    import capo_shield.types.mitigation

    out: MitigationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.mitigation.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MitigationList) -> list:
    import capo_shield.types.mitigation

    out: list = []
    for item in value:
        out.append(capo_shield.types.mitigation.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MitigationList:
    import capo_shield.types.mitigation

    out: MitigationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_shield.types.mitigation.deserialize_cbor(item))
    return out
