"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfChildBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.child_block

ListOfChildBlocks: TypeAlias = list["capo_comprehend.types.child_block.ChildBlock"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfChildBlocks) -> list:
    import capo_comprehend.types.child_block

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.child_block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfChildBlocks:
    import capo_comprehend.types.child_block

    out: ListOfChildBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.child_block.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOfChildBlocks) -> list:
    import capo_comprehend.types.child_block

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.child_block.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListOfChildBlocks:
    import capo_comprehend.types.child_block

    out: ListOfChildBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehend.types.child_block.deserialize_cbor(item))
    return out
