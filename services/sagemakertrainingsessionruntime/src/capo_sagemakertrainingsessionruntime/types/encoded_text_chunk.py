"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#EncodedTextChunk``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type
    import capo_sagemakertrainingsessionruntime.types.integer_list


class EncodedTextChunk(TypedDict, closed=True):
    tokens: "capo_sagemakertrainingsessionruntime.types.integer_list.IntegerList"
    """<p>The token IDs representing the encoded text.</p>"""
    type: "capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type.EncodedTextChunkType"
    """<p>The type of the chunk encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncodedTextChunk) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.integer_list

    out["tokens"] = (
        capo_sagemakertrainingsessionruntime.types.integer_list.serialize_json(
            value["tokens"]
        )
    )
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type

    out["type"] = (
        capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> EncodedTextChunk:
    out: EncodedTextChunk = {}  # type: ignore[typeddict-item]
    if data.get("tokens") is not None:
        import capo_sagemakertrainingsessionruntime.types.integer_list

        out["tokens"] = (
            capo_sagemakertrainingsessionruntime.types.integer_list.deserialize_json(
                data["tokens"]
            )
        )
    else:
        out["tokens"] = []
    if data.get("type") is not None:
        import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type

        out["type"] = (
            capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_type.EncodedTextChunkType",
            "",
        )
    return out
