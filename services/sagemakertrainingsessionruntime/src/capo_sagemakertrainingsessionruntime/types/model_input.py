"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#ModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list


class ModelInput(TypedDict, closed=True):
    chunks: "capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list.EncodedTextChunkList"
    """<p>The ordered list of encoded text chunks forming the input sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelInput) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list

    out["chunks"] = (
        capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list.serialize_json(
            value["chunks"]
        )
    )
    return out


def deserialize_json(data: dict) -> ModelInput:
    out: ModelInput = {}  # type: ignore[typeddict-item]
    if data.get("chunks") is not None:
        import capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list

        out["chunks"] = (
            capo_sagemakertrainingsessionruntime.types.encoded_text_chunk_list.deserialize_json(
                data["chunks"]
            )
        )
    else:
        out["chunks"] = []
    return out
