"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#EncodedTextChunkType``."""

from typing import Literal, TypeAlias, cast

EncodedTextChunkType: TypeAlias = Literal["encoded_text",]


# --- restJson1 ser/de ---
def serialize_json(value: EncodedTextChunkType) -> str:
    return value


def deserialize_json(data: str) -> EncodedTextChunkType:
    return cast(EncodedTextChunkType, data)
