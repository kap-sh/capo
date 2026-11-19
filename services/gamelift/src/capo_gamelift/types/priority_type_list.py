"""Generated from Smithy shape ``com.amazonaws.gamelift#PriorityTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.priority_type

PriorityTypeList: TypeAlias = list["capo_gamelift.types.priority_type.PriorityType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityTypeList) -> list:
    import capo_gamelift.types.priority_type

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.priority_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PriorityTypeList:
    import capo_gamelift.types.priority_type

    out: PriorityTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.priority_type.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PriorityTypeList) -> list:
    import capo_gamelift.types.priority_type

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.priority_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PriorityTypeList:
    import capo_gamelift.types.priority_type

    out: PriorityTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.priority_type.deserialize_cbor(item))
    return out
