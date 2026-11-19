"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.block

ListOfBlocks: TypeAlias = list["capo_comprehend.types.block.Block"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfBlocks) -> list:
    import capo_comprehend.types.block

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfBlocks:
    import capo_comprehend.types.block

    out: ListOfBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.block.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfBlocks) -> list:
    import capo_comprehend.types.block

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.block.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfBlocks:
    import capo_comprehend.types.block

    out: ListOfBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.block.deserialize_cbor(item))
    return out
