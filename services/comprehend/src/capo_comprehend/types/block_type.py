"""Generated from Smithy shape ``com.amazonaws.comprehend#BlockType``."""

from typing import Literal, TypeAlias, cast

BlockType: TypeAlias = Literal[
    "LINE",
    "WORD",
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
