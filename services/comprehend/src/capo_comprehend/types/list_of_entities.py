"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.entity

ListOfEntities: TypeAlias = list["capo_comprehend.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEntities) -> list:
    import capo_comprehend.types.entity

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEntities:
    import capo_comprehend.types.entity

    out: ListOfEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.entity.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfEntities) -> list:
    import capo_comprehend.types.entity

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.entity.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfEntities:
    import capo_comprehend.types.entity

    out: ListOfEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.entity.deserialize_cbor(item))
    return out
