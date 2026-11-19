"""Generated from Smithy shape ``com.amazonaws.textract#BlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.block

BlockList: TypeAlias = list["capo_textract.types.block.Block"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockList) -> list:
    import capo_textract.types.block

    out: list = []
    for item in value:
        out.append(capo_textract.types.block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BlockList:
    import capo_textract.types.block

    out: BlockList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.block.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockList) -> list:
    import capo_textract.types.block

    out: list = []
    for item in value:
        out.append(capo_textract.types.block.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BlockList:
    import capo_textract.types.block

    out: BlockList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.block.deserialize_cbor(item))
    return out
