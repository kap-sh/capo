"""Generated from Smithy shape ``com.amazonaws.textract#BlockType``."""

from typing import Literal, TypeAlias, cast

BlockType: TypeAlias = Literal[
    "KEY_VALUE_SET",
    "PAGE",
    "LINE",
    "WORD",
    "TABLE",
    "CELL",
    "SELECTION_ELEMENT",
    "MERGED_CELL",
    "TITLE",
    "QUERY",
    "QUERY_RESULT",
    "SIGNATURE",
    "TABLE_TITLE",
    "TABLE_FOOTER",
    "LAYOUT_TEXT",
    "LAYOUT_TITLE",
    "LAYOUT_HEADER",
    "LAYOUT_FOOTER",
    "LAYOUT_SECTION_HEADER",
    "LAYOUT_PAGE_NUMBER",
    "LAYOUT_LIST",
    "LAYOUT_FIGURE",
    "LAYOUT_TABLE",
    "LAYOUT_KEY_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockType:
    return cast(BlockType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockType) -> str:
    return value


def deserialize_cbor(data: str) -> BlockType:
    return cast(BlockType, data)
