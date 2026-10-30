"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#EncodedTextChunkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk

EncodedTextChunkList: TypeAlias = list[
    "capo_sagemakertrainingsessionruntime.types.encoded_text_chunk.EncodedTextChunk"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncodedTextChunkList) -> list:
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.encoded_text_chunk.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EncodedTextChunkList:
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk

    out: EncodedTextChunkList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.encoded_text_chunk.deserialize_json(
                item
            )
        )
    return out
